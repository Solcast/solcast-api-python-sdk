from .api import Client, Response
from .urls import base_url, pv_power_site, pv_power_sites


def list_pv_power_sites(**kwargs) -> Response:
    """
    Lists all PV power sites accessible to the authenticated user. Supports pagination
    (skip/take), entitlement filtering (advanced/premium), and date range filtering
    (start/end).

    Args:
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_sites, response_type=Response)

    return client.get({"format": "json", **kwargs})


def get_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Get Resource

    Args:
        resource_id: The unique identifier of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def create_pv_power_site(
    name: str,
    latitude: float,
    longitude: float,
    **kwargs,
) -> Response:
    """
    Create Resource

    Args:
        name:
        latitude:
        longitude:
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    return client.post(
        {
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "format": "json",
            **kwargs,
        }
    )


def patch_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Patch Resource

    Args:
        resource_id:
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    return client.patch({"resource_id": resource_id, "format": "json", **kwargs})


def update_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Update Resource

    Args:
        resource_id:
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    return client.put({"resource_id": resource_id, "format": "json", **kwargs})


def delete_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Remove Resource

    Args:
        resource_id: The unique identifier of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to
            the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    return client.delete({"resource_id": resource_id, "format": "json", **kwargs})
