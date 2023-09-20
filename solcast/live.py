from typing import List

from .api import Client, Response
from .urls import (
    base_url,
    live_radiation_and_weather,
    live_rooftop_pv_power,
    live_advanced_pv_power,
)


def radiation_and_weather(
    latitude: float, longitude: float, output_parameters: List[str], **kwargs
) -> Response:
    """Get irradiance and weather estimated actuals for near real-time and past 7 days
    for the requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas) and numerical weather models (other data).

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        output_parameters: list of strings with the parameters to return

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=live_radiation_and_weather)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "output_parameters": output_parameters,
        "format": "json",
        **kwargs,
    }

    res = client.get(params)

    return res


def rooftop_pv_power(latitude: float, longitude: float, **kwargs) -> Response:
    """Get basic rooftop PV power forecasts from the present time up to 14 days ahead
    for the requested location, derived from satellite (clouds and irradiance over
    non-polar continental areas, nowcasted for approx. four hours ahead) and numerical
    weather models (other data and longer horizons).

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=live_rooftop_pv_power)

    return client.get(
        {"latitude": latitude, "longitude": longitude, "format": "json", **kwargs}
    )


def advanced_pv_power(resource_id: int, **kwargs) -> Response:
    """
    Get high spec PV power forecasts from the present time up to 14 days ahead for
    the requested site, derived from satellite (clouds and irradiance
    over non-polar continental areas, nowcasted for approx. four hours ahead)
    and numerical weather models (other data and longer horizons).

    Args:
        resource_id: a Solcast resource id

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=live_advanced_pv_power)

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})
