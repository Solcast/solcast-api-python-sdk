from typing import List

from .api import Client, PandafiableResponse
from .urls import (
    base_url,
    forecast_rooftop_pv_power,
    forecast_radiation_and_weather,
    forecast_advanced_pv_power,
)


def radiation_and_weather(
    latitude: float, longitude: float, output_parameters: List[str], **kwargs
) -> PandafiableResponse:
    """
    Get irradiance and weather forecasts from the present time up to 14 days ahead
    for the requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas, nowcasted for approx. four hours ahead)
    and numerical weather models (other data and longer horizons).

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        output_parameters: list of strings with the parameters to return
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=forecast_radiation_and_weather,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "output_parameters": output_parameters,
            "format": "json",
            **kwargs,
        }
    )


def rooftop_pv_power(
    latitude: float, longitude: float, output_parameters: List[str], **kwargs
) -> PandafiableResponse:
    """
    Get basic rooftop PV power forecasts from the present time up to 14 days ahead
    for the requested location, derived from satellite (clouds and irradiance
    over non-polar continental areas, nowcasted for approx. four hours ahead)
    and numerical weather models (other data and longer horizons).

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        output_parameters: list of strings with the parameters to return
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=forecast_rooftop_pv_power,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "output_parameters": output_parameters,
            "format": "json",
            **kwargs,
        }
    )


def advanced_pv_power(resource_id: int, **kwargs) -> PandafiableResponse:
    """
    Get high spec PV power forecasts from the present time up to 14 days ahead
    for the requested site, derived from satellite (clouds and irradiance over
    non-polar continental areas, nowcasted for approx. four hours ahead) and
    numerical weather models (other data and longer horizons).

    Args:
        resource_id: a Solcast resource id
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=forecast_advanced_pv_power,
        response_type=PandafiableResponse,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})
