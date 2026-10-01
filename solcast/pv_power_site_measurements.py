from ._site_measurements import MeasurementInput, measurement_records
from .api import Client, PandafiableResponse, Response
from .urls import (
    base_url,
    pv_power_site_measurements,
    pv_power_site_measurements_sub_units,
)


def create_pv_site_measurements(
    resource_id: str, measurements: MeasurementInput, **kwargs
) -> Response:
    """
    Submit measurement data for a Premium PV Power site. Measurements are used for model
    training. Maximum 1000 measurements per request. Power units (AC) are measured in
    MW. Power is the actual measured power output by the site. If there are availability
    and curtailment constraints in place, those fields should also be included with the
    measurements.

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        measurements: Array of measurement records (1-1000).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#postResourcesPvPowerSiteMeasurements.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements,
        response_type=Response,
    )

    records = measurement_records(measurements)

    return client.post(
        {"format": "json", **kwargs},
        json_body={
            "resource_id": resource_id,
            "measurements": records,
        },
    )


def get_pv_site_measurements(resource_id: str, **kwargs) -> PandafiableResponse:
    """
    Retrieve historical measurement data for a Premium PV Power site. Supports
    pagination via skip/take and date filtering via start/end.

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#getResourcesPvPowerSiteMeasurements.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements,
        response_type=PandafiableResponse,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def delete_pv_site_measurements(
    resource_id: str, start: str, end: str, **kwargs
) -> Response:
    """
    Delete site measurements

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        start: Delete lower bound timestamp (ISO-8601).
        end: Delete upper bound timestamp (ISO-8601).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#deleteResourcesPvPowerSiteMeasurements.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements,
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


def create_pv_sub_unit_measurements(
    resource_id: str, measurements: MeasurementInput, **kwargs
) -> Response:
    """
    Submit sub-unit measurement data for a Premium PV Power site. A sub-unit represents
    a subsection of the site, such as an individual inverter or a subset of inverters.
    Each measurement must include a 'sub_unit' label. Maximum 1000 measurements per
    request. Power units (AC) are measured in MW.

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        measurements: List of sub-unit measurement records (1-1000).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#postResourcesPvPowerSiteMeasurementsSubUnits.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements_sub_units,
        response_type=Response,
    )

    records = measurement_records(measurements)

    return client.post(
        {"format": "json", **kwargs},
        json_body={
            "resource_id": resource_id,
            "measurements": records,
        },
    )


def get_pv_sub_unit_measurements(resource_id: str, **kwargs) -> PandafiableResponse:
    """
    Retrieve historical sub-unit measurement data for a Premium PV Power site. A
    sub-unit represents a subsection of the site, such as an individual inverter or a
    subset of inverters. Supports pagination via skip/take, date filtering via
    start/end, and an optional sub_unit filter.

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#getResourcesPvPowerSiteMeasurementsSubUnits.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements_sub_units,
        response_type=PandafiableResponse,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def delete_pv_sub_unit_measurements(
    resource_id: str, start: str, end: str, **kwargs
) -> Response:
    """
    Delete sub-unit site measurements

    Args:
        resource_id: The unique identifier of the Premium PV Power resource.
        start: Delete lower bound timestamp (ISO-8601).
        end: Delete upper bound timestamp (ISO-8601).
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#deleteResourcesPvPowerSiteMeasurementsSubUnits.
    """
    client = Client(
        base_url=base_url,
        endpoint=pv_power_site_measurements_sub_units,
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
