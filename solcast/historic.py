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
    Get historical irradiance and weather estimated actuals for up to 31 days of data
    at a time for a requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas) and numerical weather models (other data).
    Data is available from 2007-01-01T00:00Z up to real time estimated actuals.

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        start: datetime-like, first day of the requested period
        end: optional, datetime-like, last day of the requested period
        duration: optional, ISO_8601 compliant duration for the historic data.
            Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(
        base_url=base_url,
        endpoint=historic_radiation_and_weather,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
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
    derived from satellite (clouds and irradiance over non-polar continental areas)
    and numerical weather models (other data).

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        start: datetime-like, first day of the requested period
        end: optional, datetime-like, last day of the requested period
        duration: optional, ISO_8601 compliant duration for the historic data.
            Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(
        base_url=base_url,
        endpoint=historic_rooftop_pv_power,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
    )

    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

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
    Get historical high spec PV power estimated actuals for the requested site,
    derived from satellite (clouds and irradiance over non-polar continental areas)
    and numerical weather models (other data).

    Args:
        resource_id: a Solcast resource id
        start: datetime-like, first day of the requested period
        end: optional, datetime-like, last day of the requested period
        duration: optional, ISO_8601 compliant duration for the historic data.
            Must be within 31 days of the start_date.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=historic_advanced_pv_power,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
    )

    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    params = {
        "resource_id": resource_id,
        "start": start,
        "format": "json",
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
    """Get hourly historical soiling loss using the Kimber model.

    Returns a time series of estimated historical cumulative soiling / cleanliness state
    for the requested location based on Pvlib's Kimber model.

    Args:
        latitude: Decimal degrees, between -90 and 90 (north positive).
        longitude: Decimal degrees, between -180 and 180 (east positive).
        start: Datetime-like (YYYY-MM-DD or ISO8601) start of period.
        end: Optional, end of requested period (mutually exclusive with duration).
        duration: Optional, ISO8601 duration within 31 days of start (mutually exclusive with end).
        **kwargs: Additional query parameters accepted by the endpoint (e.g. depo_veloc_pm10, initial_soiling).

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full parameter details.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    url = kwargs.pop("base_url", base_url)
    client = Client(
        base_url=url,
        endpoint=historic_soiling_kimber,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
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
    """Get hourly historical soiling loss using the HSU model.

    Returns a time series of estimated historical cumulative soiling / cleanliness state
    for the requested location based on Solcast's HSU model.

    Args:
        latitude: Decimal degrees, between -90 and 90 (north positive).
        longitude: Decimal degrees, between -180 and 180 (east positive).
        start: Datetime-like (YYYY-MM-DD or ISO8601) start of period.
        end: Optional, end of requested period (mutually exclusive with duration).
        duration: Optional, ISO8601 duration within 31 days of start (mutually exclusive with end).
        **kwargs: Additional query parameters accepted by the endpoint (e.g. depo_veloc_pm10, initial_soiling).

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full parameter details.
    """
    assert (end is None and duration is not None) | (
        duration is None and end is not None
    ), "only one of duration or end"

    url = kwargs.pop("base_url", base_url)
    client = Client(
        base_url=url,
        endpoint=historic_soiling_hsu,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
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
