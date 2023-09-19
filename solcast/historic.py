from .api import Client, Response
from .urls import base_url, historic_radiation_and_weather, historic_rooftop_pv_power


def radiation_and_weather(
    latitude: float,
    longitude: float,
    start: str,
    end: str = None,
    duration: str = None,
    **kwargs,
) -> Response:
    """
    Get historical irradiance and weather estimated actuals for up to 31 days of data
    at a time for a requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas) and numerical weather models (other data).
    Data is available from 2007-01-01T00:00Z up to real time estimated actuals.

    To define the length of the period you can use one of "end" or "duration" parameter.

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(base_url=base_url, endpoint=historic_radiation_and_weather)

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


def rooftop_pv_power(
    latitude: float,
    longitude: float,
    start: str,
    end: str = None,
    duration: str = None,
    **kwargs,
) -> Response:
    """
    Get historical basic rooftop PV power estimated actuals for the requested location,
    derived from satellite (clouds and irradiance over non-polar continental areas)
    and numerical weather models (other data).

    To define the length of the period you can use one of "end" or "duration" parameter.

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(base_url=base_url, endpoint=historic_rooftop_pv_power)

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
