import copy
import json
import os
import urllib.error
import urllib.parse
from dataclasses import dataclass
from typing import Optional, Tuple
from urllib.request import Request, urlopen

import solcast


@dataclass
class Response:
    """Class to handle any API response from the Solcast API.

    Attributes:
        code: HTTP status code of the response
        url: The URL that was requested
        data: Raw response data as bytes
        success: Whether the request was successful
        method: HTTP method used (GET, POST, etc.)
        exception: Exception message if request failed

    Examples:
        >>> response = Response(code=200, url="...", data=b"...", success=True, method="GET")
        >>> response.to_dict()
    """

    code: int
    url: str
    data: Optional[bytes]
    success: bool
    method: str
    exception: Optional[str] = None

    def __repr__(self):
        return f"status code={self.code}, url={self.url}, method={self.method}"

    def to_dict(self):
        """Return the data as a dictionary."""
        if self.code not in [200, 204]:
            raise Exception(self.exception)
        if self.code == 204:
            return dict()
        return json.loads(self.data)

    def __call__(self, *args, **kwargs) -> "Response":
        return type(self)(*args, **kwargs)


class PandafiableResponse(Response):
    """Class to handle API response from the Solcast API for timeseries data.

    Attributes:
        code: HTTP status code of the response
        url: The URL that was requested
        data: Raw response data as bytes
        success: Whether the request was successful
        method: HTTP method used (GET, POST, etc.)
        exception: Exception message if request failed

    Examples:
        >>> response = Response(code=200, url="...", data=b"...", success=True, method="GET")
        >>> response.to_pandas()
    """

    def to_pandas(self):
        """Return the data as a Pandas DataFrame with a DatetimeIndex."""
        # not ideal to run this for every Response

        try:
            import pandas as pd
        except ImportError as e:
            raise ImportError(
                f"Pandas needs to be installed for this functionality. {e}"
            )

        if self.code != 200:
            raise Exception(self.exception)

        dfs = [
            pd.DataFrame.from_records(self.to_dict()[k]) for k in self.to_dict().keys()
        ]
        dfs = pd.concat(dfs)
        dfs.index = pd.DatetimeIndex(dfs["period_end"])

        # to make it work with different Pandas versions
        if dfs.index.tz is None:
            dfs.index = dfs.index.tz_localize("UTC")

        dfs.index.name = "period_end"
        dfs = dfs.drop(columns=["period_end", "period"])

        return dfs

    def __call__(self, *args, **kwargs) -> "PandafiableResponse":
        return type(self)(*args, **kwargs)


class Client:
    """Handles all API get requests for the different endpoints."""

    def __init__(
        self,
        base_url: str,
        endpoint: str,
        response_type: Response,
    ):
        """
        Args:
            base_url: the base URL to Solcast API
            endpoint: one of Solcast API's endpoints
        """
        self.base_url = base_url
        self.endpoint = endpoint
        self.user_agent = f"solcast-api-python-sdk/{solcast.__version__}"
        self.response = response_type
        self.url = self.make_url()

    @staticmethod
    def _check_params(params: dict) -> Tuple[dict, str]:
        """Run basic checks on the parameters that will be passed to the HTTP request."""
        assert isinstance(params, dict), "parameters needs to be a dict"
        params = copy.deepcopy(params)

        if "api_key" in params:
            # api key in the header for secrecy
            key = params["api_key"]
            del params["api_key"]
        else:
            key = os.getenv("SOLCAST_API_KEY")

        if key is None:
            raise ValueError(
                "no API key provided. Either set it as an environment "
                "variable SOLCAST_API_KEY, or provide `api_key` "
                "as an argument. Visit https://solcast.com to get an API key."
            )

        if len(key) <= 1:
            raise ValueError("API key is too short.")

        if "output_parameters" in params.keys() and isinstance(
            params["output_parameters"], list
        ):
            params["output_parameters"] = ",".join(params["output_parameters"])

        # truncate coordinates to 6 decimal places
        if "latitude" in params.keys():
            params["latitude"] = round(params["latitude"], 6)
        if "longitude" in params.keys():
            params["longitude"] = round(params["longitude"], 6)

        # only json supported
        if "format" in params.keys():
            if params["format"] != "json":
                raise NotImplementedError(
                    "Only json response format is currently supported."
                )

        return params, key

    def make_url(self) -> str:
        """Compose the full URL."""
        return "/".join([self.base_url, self.endpoint])

    def get(self, params: dict) -> Response:
        """Wrap _make_request to make a GET request

        Args:
            params: a dictionary of parameters that are passed in the GET request

        Returns:
            a Response object.

        """
        return self._make_request(params, method="GET")

    def post(self, params: dict) -> Response:
        """Wrap _make_request to make a POST request

        Args:
            params: a dictionary of parameters that are passed in the POST request

        Returns:
            a Response object.

        """
        return self._make_request(params, method="POST")

    def patch(self, params: dict) -> Response:
        """Wrap _make_request to make a PATCH request

        Args:
            params: a dictionary of parameters that are passed in the PATCH request

        Returns:
            a Response object.

        """
        return self._make_request(params, method="PATCH")

    def put(self, params: dict) -> Response:
        """Wrap _make_request to make a PUT request

        Args:
            params: a dictionary of parameters that are passed in the PUT request

        Returns:
            a Response object.

        """
        return self._make_request(params, method="PUT")

    def delete(self, params: dict) -> Response:
        """Wrap _make_request to make a DEL request

        Args:
            params: a dictionary of parameters that are passed in the DEL request

        Returns:
            a Response object.

        """
        return self._make_request(params, method="DELETE")

    def _make_request(self, params: dict, method: str) -> Response:
        """Make a request using urllib with the HTTP method specified

        Args:
            params: a dictionary of parameters that are passed in the request
            method: HTTP method to use

        Returns:
            a Response object.
        """

        params, key = self._check_params(params)
        url = self.url + "?" + urllib.parse.urlencode(params)
        req = Request(
            url,
            headers={"Authorization": f"Bearer {key}", "User-Agent": self.user_agent},
            method=method,
        )
        try:
            with urlopen(req) as response:
                body = response.read()
                return self.response(
                    code=response.code,
                    url=url,
                    data=body,
                    success=True,
                    exception=None,
                    method=method,
                )
        except urllib.error.HTTPError as e:
            try:
                exception_message = json.loads(e.read())["response_status"]["message"]
            except Exception:
                exception_message = "Undefined Error"
            return self.response(
                code=e.code,
                url=e.url,
                data=None,
                exception=exception_message,
                success=False,
                method=method,
            )
