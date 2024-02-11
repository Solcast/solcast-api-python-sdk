from .api import Client, PandafiableResponse
from .urls import base_url, tmy_radiation_and_weather, tmy_rooftop_pv_power


def radiation_and_weather(
    latitude: float, longitude: float, **kwargs
) -> PandafiableResponse:
    """
    Get the irradiance and weather for a Typical Meteorological Year (TMY) at a requested location,
    derived from satellite (clouds and irradiance over non-polar continental areas) and
    numerical weather models (other data). The TMY is calculated with data from 2007 to 2023.

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(
        base_url=base_url,
        endpoint=tmy_radiation_and_weather,
        response_type=PandafiableResponse,
    )

    return client.get(
        {"latitude": latitude, "longitude": longitude, "format": "json", **kwargs}
    )


def rooftop_pv_power(
    latitude: float, longitude: float, **kwargs
) -> PandafiableResponse:
    """
    Get the basic rooftop PV power estimated actuals for a Typical Meteorological Year (TMY) at a requested location,
    derived from satellite (clouds and irradiance over non-polar continental areas) and
    numerical weather models (other data). The TMY is calculated with data from 2007 to 2023.

    Args:
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """

    client = Client(
        base_url=base_url,
        endpoint=tmy_rooftop_pv_power,
        response_type=PandafiableResponse,
    )

    return client.get(
        {"latitude": latitude, "longitude": longitude, "format": "json", **kwargs}
    )
