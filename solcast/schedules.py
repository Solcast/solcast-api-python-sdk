from typing import Any, Dict, List, Optional

from .api import Client, Response
from .urls import base_url, resource_schedule


def delete_resource_schedule(
    resource_id: str, period_start: str, period_end: str, schedule_type: str, **kwargs
) -> Response:
    """
    Remove stored schedule data for the given time window and schedule type(s).
    Intervals extending beyond the window are trimmed; intervals entirely within are
    dropped.

    Args:
        resource_id: The resource id.
        period_start: Start of the delete window (ISO 8601). Must be on a 5-minute boundary.
        period_end: End of the delete window (ISO 8601). Must be on a 5-minute boundary.
        schedule_type: Comma-separated list of schedule types to delete: availability, curtailment
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#deleteManageSchedules.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=resource_schedule,
        response_type=Response,
    )

    return client.delete(
        {
            "resource_id": resource_id,
            "period_start": period_start,
            "period_end": period_end,
            "schedule_type": schedule_type,
            **kwargs,
        }
    )


def get_resource_schedule(
    resource_id: str,
    period_start: str,
    period_end: str,
    issue_time: Optional[str] = None,
    **kwargs,
) -> Response:
    """
    Retrieve the current availability and curtailment schedule for a premium resource.
    Use issue_time to query historical schedule state.

    Args:
        resource_id: The resource id.
        period_start: Start of the query window (ISO 8601). Must be on a 5-minute boundary.
        period_end: End of the query window (ISO 8601). Must be on a 5-minute boundary.
        issue_time: Return the schedule as it existed at this point in time (ISO 8601).
            When omitted, the latest schedule is returned.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#getManageSchedules.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=resource_schedule,
        response_type=Response,
    )

    return client.get(
        {
            "resource_id": resource_id,
            "period_start": period_start,
            "period_end": period_end,
            **({"issue_time": issue_time} if issue_time is not None else {}),
            "format": "json",
            **kwargs,
        }
    )


def patch_resource_schedule(
    resource_id: str,
    availability_schedule: Optional[List[Dict[str, Any]]] = None,
    curtailment_schedule: Optional[List[Dict[str, Any]]] = None,
    **kwargs,
) -> Response:
    """
    Merge new availability and/or curtailment schedule intervals into the existing
    stored schedule for a premium resource. Overlapping intervals are replaced (existing
    intervals are split as needed). The request is all-or-nothing: a validation error in
    any entry rejects the entire request.

    Args:
        resource_id: The resource id.
        availability_schedule: Availability schedule entries to merge.
        curtailment_schedule: Curtailment schedule entries to merge.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#patchManageSchedules.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=resource_schedule,
        response_type=Response,
    )

    request_body = {
        "resource_id": resource_id,
    }
    if availability_schedule is not None:
        request_body["availability_schedule"] = availability_schedule
    if curtailment_schedule is not None:
        request_body["curtailment_schedule"] = curtailment_schedule
    return client.patch(
        {**kwargs},
        json_body=request_body,
    )
