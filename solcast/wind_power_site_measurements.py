from typing import Any, Dict, List

from .api import Client, Response
from .urls import (
    base_url,
    wind_power_site_measurements,
    wind_power_site_measurements_sub_units,
)


def create_wind_site_measurements(
    resource_id: str, measurements: List[Dict[str, Any]], **kwargs
) -> Response:
    """
    Submit measurement data for a Premium Wind Power site. Measurements are used for
    model training. Maximum 1000 measurements per request. Power units (AC) are measured
    in MW. Power is the actual measured power output by the site. If there are
    availability and curtailment constraints in place, those fields should also be
    included with the measurements.

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        measurements: Array of measurement records (1-1000).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements,
        response_type=Response,
    )

    return client.post(
        {"format": "json", **kwargs},
        json_body={
            "resource_id": resource_id,
            "measurements": measurements,
        },
    )


def get_wind_site_measurements(resource_id: str, **kwargs) -> Response:
    """
    Retrieve historical measurement data for a Premium Wind Power site. Supports
    pagination via skip/take and date filtering via start/end.

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements,
        response_type=Response,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def delete_wind_site_measurements(
    resource_id: str, start: str, end: str, **kwargs
) -> Response:
    """
    Delete site measurements

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        start: Delete lower bound timestamp (ISO-8601).
        end: Delete upper bound timestamp (ISO-8601).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements,
        response_type=Response,
    )

    return client.delete(
        {
            "resource_id": resource_id,
            "start": start,
            "end": end,
            "format": "json",
            **kwargs,
        }
    )


def create_wind_sub_unit_site_measurements(
    resource_id: str, measurements: List[Dict[str, Any]], **kwargs
) -> Response:
    """
    Submit sub-unit measurement data for a Premium Wind Power site. A sub-unit
    represents a subsection of the site, such as an individual wind turbine or a subset
    of turbines. Each measurement must include a 'sub_unit' label. Maximum 1000
    measurements per request. Power units (AC) are measured in MW.

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        measurements: List of sub-unit measurement records (1-1000).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements_sub_units,
        response_type=Response,
    )

    return client.post(
        {"format": "json", **kwargs},
        json_body={
            "resource_id": resource_id,
            "measurements": measurements,
        },
    )


def get_wind_sub_unit_site_measurements(resource_id: str, **kwargs) -> Response:
    """
    Retrieve historical sub-unit measurement data for a Premium Wind Power site. A
    sub-unit represents a subsection of the site, such as an individual wind turbine or
    a subset of turbines. Supports pagination via skip/take, date filtering via
    start/end, and an optional sub_unit filter.

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements_sub_units,
        response_type=Response,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def delete_wind_sub_unit_site_measurements(
    resource_id: str, start: str, end: str, **kwargs
) -> Response:
    """
    Delete sub-unit site measurements

    Args:
        resource_id: The unique identifier of the Premium Wind Power resource.
        start: Delete lower bound timestamp (ISO-8601).
        end: Delete upper bound timestamp (ISO-8601).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=wind_power_site_measurements_sub_units,
        response_type=Response,
    )

    return client.delete(
        {
            "resource_id": resource_id,
            "start": start,
            "end": end,
            "format": "json",
            **kwargs,
        }
    )
