import json
import os
from dataclasses import dataclass
from urllib.request import urlopen, Request
import urllib.parse
import urllib.error
from typing import Optional

import solcast

try:
    import pandas as pd
except ImportError:
    _PANDAS = False
else:
    _PANDAS = True


@dataclass
class Response:
    """Class to handle API response from the Solcast API."""

    code: int
    url: str
    data: Optional[bytes]
    success: bool
    exception: Optional[str] = None

    def __repr__(self):
        return f"status code={self.code}, url={self.url}"

    def to_dict(self):
        if self.code != 200:
            raise Exception(self.exception)
        return json.loads(self.data)

    def to_pandas(self):
        """returns the data as a Pandas DataFrame.
        Some common processing is applied,
        like casting the datetime columns and setting them as index.
        """
        # not ideal to run this for every Response
        assert _PANDAS, ImportError(
            "Pandas needs to be installed for this functionality."
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
            dfs.index.tz = "UTC"

        dfs.index.name = "period_end"
        dfs = dfs.drop(columns=["period_end", "period"])

        return dfs


class Client:
    """Handles all API get requests for the different endpoints."""

    def __init__(self, base_url: str, endpoint: str):
        """
        Args:
            base_url: the base URL to Solcast API
            endpoint: one of Solcast API's endpoints
        """
        self.base_url = base_url
        self.endpoint = endpoint
        self.user_agent = f"solcast-api-python-sdk/{solcast.__version__}"
        self.url = self.make_url()

    @staticmethod
    def check_params(params: dict) -> (dict, str):
        """runs some basic checks on the parameters that will be passed in the
        GET request."""
        assert isinstance(params, dict), "parameters needs to be a dict"

        if "api_key" not in params:
            params.update({"api_key": os.getenv("SOLCAST_API_KEY")})

        if params["api_key"] is None:
            raise ValueError(
                "no API key provided. Either set it as an environment "
                "variable SOLCAST_API_KEY, or provide `api_key` "
                "as an argument. Visit https://solcast.com to get an API key."
            )

        if len(params["api_key"]) <= 1:
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
            assert (
                params["format"] == "json"
            ), "only json response format is currently supported."

        # api key in the header for secrecy
        key = params["api_key"]
        del params["api_key"]

        return params, key

    def make_url(self) -> str:
        """composes the full URL."""
        return "/".join([self.base_url, self.endpoint])

    def get(self, params: dict) -> Response:
        """makes the GET request.

        Args:
            params: a dictionary of parameters that are passed in the get request

        Returns:
            a Response object.
        """

        params, key = self.check_params(params)
        url = self.url + "?" + urllib.parse.urlencode(params)
        req = Request(
            url,
            headers={"Authorization": f"Bearer {key}", "User-Agent": self.user_agent},
        )
        try:
            with urlopen(req) as response:
                body = response.read()
                return Response(
                    code=response.code, url=url, data=body, success=True, exception=None
                )
        except urllib.error.HTTPError as e:
            try:
                exception_message = json.loads(e.read())["response_status"]["message"]
            except:
                exception_message = "Undefined Error"
            return Response(
                code=e.code,
                url=e.url,
                data=None,
                exception=exception_message,
                success=False,
            )
