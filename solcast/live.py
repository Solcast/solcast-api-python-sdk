from typing import List

from .api import Client, PandafiableResponse
from .urls import (
    base_url,
    live_advanced_pv_power,
    live_radiation_and_weather,
    live_rooftop_pv_power,
    live_soiling_hsu,
    live_soiling_kimber,
)


def radiation_and_weather(
    latitude: float, longitude: float, output_parameters: List[str], **kwargs
) -> PandafiableResponse:
    """
    Get irradiance and weather estimated actuals for near real-time and past 7 days for
    the requested location, derived from satellite (clouds and irradiance over non-polar
    continental areas) and numerical weather models (other data).

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        output_parameters: The output parameters to include in the response.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=live_radiation_and_weather,
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
    latitude: float, longitude: float, **kwargs
) -> PandafiableResponse:
    """
    Get basic rooftop PV power estimated actuals for near real-time and past 7 days for
    the requested location, derived from satellite (clouds and irradiance over non-polar
    continental areas) and numerical weather models (other data).

    The basic rooftop power simulation is only suitable for residential and smaller C&I
    rooftop sites, not for grid-scale sites.

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=live_rooftop_pv_power,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )


def advanced_pv_power(resource_id: int, **kwargs) -> PandafiableResponse:
    """
    Get high spec PV power estimated actuals for near real-time and past 7 days for the
    requested site, derived from satellite (clouds and irradiance over non-polar
    continental areas) and numerical weather models (other data).

    Args:
        resource_id: The resource id of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=live_advanced_pv_power,
        response_type=PandafiableResponse,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def soiling_hsu(
    latitude: float,
    longitude: float,
    **kwargs,
) -> PandafiableResponse:
    """
    Get soiling loss estimated actuals using the HSU model for near real-time and past 7
    days for the requested location.

    Args:
        latitude: The latitude of the location you request data for. Must be a decimal
            number between -90 and 90.
        longitude: The longitude of the location you request data for. Must be a decimal
            number between -180 and 180.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=live_soiling_hsu,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )


def soiling_kimber(
    latitude: float,
    longitude: float,
    base_url=base_url,
    **kwargs,
) -> PandafiableResponse:
    """
    Get soiling loss estimated actuals using the Kimber model for near real-time and
    past 7 days for the requested location.

    Args:
        latitude: The latitude of the location (EPSG:4326). Must be between -90 and 90.
        longitude: The longitude of the location (EPSG:4326). Must be between -180 and
            180.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=live_soiling_kimber,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )
