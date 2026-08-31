from typing import Optional

from .api import Client, PandafiableResponse
from .urls import (
    base_url,
    historic_advanced_pv_power,
    historic_radiation_and_weather,
    historic_rooftop_pv_power,
    historic_soiling_hsu,
    historic_soiling_kimber,
)


def radiation_and_weather(
    latitude: float,
    longitude: float,
    start: str,
    end: Optional[str] = None,
    duration: Optional[str] = None,
    **kwargs,
) -> PandafiableResponse:
    """
    Get historical irradiance and weather estimated actuals for up to 31 days of data at
    a time for a requested location, derived from satellite (clouds and irradiance over
    non-polar continental areas) and numerical weather models (other data). Data is
    available from 2007-01-01T00:00Z to 7 days ago.

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        start: ISO_8601 compliant starting datetime for the historical data. If the
            supplied value does not specify a timezone, the timezone will be inferred
            from the time_zone parameter, if supplied. Otherwise UTC is assumed.
        end: Must include one of end_date and duration. ISO_8601 compliant ending
            datetime for the historical data. Must be within 31 days of the start_date.
            If the supplied value does not specify a timezone, the timezone will be
            inferred from the time_zone parameter, if supplied. Otherwise UTC is
            assumed.
        duration: Must include one of end_date and duration. ISO_8601 compliant duration
            for the historical data. Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    client = Client(
        base_url=base_url,
        endpoint=historic_radiation_and_weather,
        response_type=PandafiableResponse,
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "format": "json",
        **kwargs,
    }

    if end is not None:
        params["end"] = end
    if duration is not None:
        params["duration"] = duration

    return client.get(params)


def rooftop_pv_power(
    latitude: float,
    longitude: float,
    start: str,
    end: Optional[str] = None,
    duration: Optional[str] = None,
    **kwargs,
) -> PandafiableResponse:
    """
    Get historical basic rooftop PV power estimated actuals for the requested location,
    derived from satellite (clouds and irradiance over non-polar continental areas) and
    numerical weather models (other data). Data is available from 2007-01-01T00:00Z to 7
    days ago.

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        start: ISO_8601 compliant starting datetime for the historical data. If the
            supplied value does not specify a timezone, the timezone will be inferred
            from the time_zone parameter, if supplied. Otherwise UTC is assumed.
        end: Must include one of end_date and duration. ISO_8601 compliant ending
            datetime for the historical data. Must be within 31 days of the start_date.
            If the supplied value does not specify a timezone, the timezone will be
            inferred from the time_zone parameter, if supplied. Otherwise UTC is
            assumed.
        duration: Must include one of end_date and duration. ISO_8601 compliant duration
            for the historical data. Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    client = Client(
        base_url=base_url,
        endpoint=historic_rooftop_pv_power,
        response_type=PandafiableResponse,
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "format": "json",
        **kwargs,
    }

    if end is not None:
        params["end"] = end
    if duration is not None:
        params["duration"] = duration

    return client.get(params)


def advanced_pv_power(
    resource_id: int,
    start: str,
    end: Optional[str] = None,
    duration: Optional[str] = None,
    **kwargs,
) -> PandafiableResponse:
    """
    Get historical advanced PV power estimated actuals for the requested location,
    derived from satellite (clouds and irradiance over non-polar continental areas) and
    numerical weather models (other data). Data is available from 2007-01-01T00:00Z to 7
    days ago.

    Args:
        resource_id: The resource id of the resource.
        start: ISO_8601 compliant starting datetime for the historical data. If the
            supplied value does not specify a timezone, the timezone will be inferred
            from the time_zone parameter, if supplied. Otherwise UTC is assumed.
        end: Must include one of end_date and duration. ISO_8601 compliant ending
            datetime for the historical data. Must be within 31 days of the start_date.
            If the supplied value does not specify a timezone, the timezone will be
            inferred from the time_zone parameter, if supplied. Otherwise UTC is
            assumed.
        duration: Must include one of end_date and duration. ISO_8601 compliant duration
            for the historical data. Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    client = Client(
        base_url=base_url,
        endpoint=historic_advanced_pv_power,
        response_type=PandafiableResponse,
    )

    params = {
        "resource_id": resource_id,
        "start": start,
        "format": "json",
        **kwargs,
    }

    if end is not None:
        params["end"] = end
    if duration is not None:
        params["duration"] = duration

    return client.get(params)


def soiling_kimber(
    latitude: float,
    longitude: float,
    start: str,
    end: Optional[str] = None,
    duration: Optional[str] = None,
    **kwargs,
) -> PandafiableResponse:
    """
    Get historical soiling loss using the Kimber model for up to 31 days of data at a
    time for a requested location. Data is available from 2007-01-01T00:00Z to 7 days
    ago.

    Args:
        latitude: The latitude of the location (EPSG:4326). Must be between -90 and 90.
        longitude: The longitude of the location (EPSG:4326). Must be between -180 and
            180.
        start: ISO_8601 compliant starting datetime for the historical data. If the
            supplied value does not specify a timezone, the timezone will be inferred
            from the time_zone parameter, if supplied. Otherwise UTC is assumed.
        end: ISO_8601 compliant ending datetime for the historical data. Must be within
            31 days of the start_date. Only one of end or duration should be part of the
            request. If the supplied value does not specify a timezone, the timezone
            will be inferred from the time_zone parameter, if supplied. Otherwise UTC is
            assumed.
        duration: ISO_8601 compliant duration for the historical data. Must be within 31
            days of the start_date. Only one of end or duration should be part of the
            request.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=historic_soiling_kimber,
        response_type=PandafiableResponse,
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "format": "json",
        **kwargs,
    }

    if end is not None:
        params["end"] = end
    if duration is not None:
        params["duration"] = duration

    return client.get(params)


def soiling_hsu(
    latitude: float,
    longitude: float,
    start: str,
    end: Optional[str] = None,
    duration: Optional[str] = None,
    base_url=base_url,
    **kwargs,
) -> PandafiableResponse:
    """
    Get historical soiling loss using the HSU model for up to 31 days of data at a time
    for a requested location. Data is available from 2007-01-01T00:00Z to 7 days ago.

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        start: ISO_8601 compliant starting datetime for the historical data. If the
            supplied value does not specify a timezone, the timezone will be inferred
            from the time_zone parameter, if supplied. Otherwise UTC is assumed.
        end: ISO_8601 compliant ending datetime for the historical data. Must be within
            31 days of the start_date. Only one of end or duration should be part of the
            request. If the supplied value does not specify a timezone, the timezone
            will be inferred from the time_zone parameter, if supplied. Otherwise UTC is
            assumed.
        duration: ISO_8601 compliant duration for the historical data. Must be within 31
            days of the start_date. Only one of end or duration should be part of the
            request.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=historic_soiling_hsu,
        response_type=PandafiableResponse,
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "format": "json",
        **kwargs,
    }

    if end is not None:
        params["end"] = end
    if duration is not None:
        params["duration"] = duration

    return client.get(params)
