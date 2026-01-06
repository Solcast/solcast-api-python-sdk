from typing import List

from .api import Client, PandafiableResponse
from .urls import (
    base_url,
    forecast_advanced_pv_power,
    forecast_radiation_and_weather,
    forecast_rooftop_pv_power,
    forecast_soiling_hsu,
    forecast_soiling_kimber,
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
        response_type=PandafiableResponse,  # type: ignore[arg-type]
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
        response_type=PandafiableResponse,  # type: ignore[arg-type]
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
        response_type=PandafiableResponse,  # type: ignore[arg-type]
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def soiling_kimber(
    latitude: float,
    longitude: float,
    **kwargs,
) -> PandafiableResponse:
    """Get hourly soiling loss forecast using the Kimber model.

    Returns a time series of forecast cumulative soiling / cleanliness state for the
    requested location based on Pvlib's Kimber model.

    Args:
        latitude: Decimal degrees, between -90 and 90 (north positive).
        longitude: Decimal degrees, between -180 and 180 (east positive).
        **kwargs: Additional query parameters accepted by the endpoint (e.g. depo_veloc_pm10, initial_soiling).

    Returns:
        PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full parameter details.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=forecast_soiling_kimber,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
    )
    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )


def soiling_hsu(
    latitude: float,
    longitude: float,
    **kwargs,
) -> PandafiableResponse:
    """Get hourly soiling loss forecast using the HSU model.

     Returns a time series of forecast cumulative soiling / cleanliness state for the
     requested location based on Solcast's HSU model.

     Args:
         latitude: Decimal degrees, between -90 and 90 (north positive).
         longitude: Decimal degrees, between -180 and 180 (east positive).
         **kwargs: Additional query parameters accepted by the endpoint (e.g. depo_veloc_pm10, initial_soiling).

     Returns:
         PandafiableResponse: Response object; call `.to_pandas()` for a DataFrame.

    See https://docs.solcast.com.au/ for full parameter details.
    """
    url = kwargs.pop("base_url", base_url)
    client = Client(
        base_url=url,
        endpoint=forecast_soiling_hsu,
        response_type=PandafiableResponse,  # type: ignore[arg-type]
    )
    return client.get(
        {
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )
