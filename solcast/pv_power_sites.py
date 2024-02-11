from .api import Client, Response
from .urls import base_url, pv_power_site, pv_power_sites


def list_pv_power_sites(**kwargs) -> Response:
    """
    List available PV power sites.

    Args:
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_sites, response_type=Response)

    params = {"format": "json", **kwargs}

    res = client.get(params)

    return res


def get_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Get an existing PV power site's specifications.

    Args:
        resource_id: unique string to identify the location that was generated when creating a site
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    params = {"resource_id": resource_id, "format": "json", **kwargs}

    res = client.get(params)

    return res


def create_pv_power_site(
    name: str,
    latitude: float,
    longitude: float,
    **kwargs,
) -> Response:
    """
    Create PV power site to be used with Solcast's advanced PV power model.

    Args:
        name: arbitrary string to identify the location, unique not required
        latitude: in decimal degrees, between -90 and 90, north is positive
        longitude: in decimal degrees, between -180 and 180, east is positive
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for more information and full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    params = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "format": "json",
        **kwargs,
    }

    res = client.post(params)

    return res


def patch_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Patch an existing PV power site to partially update the site's specifications.

    Args:
        resource_id: unique string to identify the location that is generated when creating a site
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    params = {
        "resource_id": resource_id,
        "format": "json",
        **kwargs,
    }

    res = client.patch(params)

    return res


def update_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Overwrite an existing PV power site's specifications.

    Args:
        resource_id: unique string to identify the location that is generated when creating a site
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    params = {
        "resource_id": resource_id,
        "format": "json",
        **kwargs,
    }

    res = client.put(params)

    return res


def delete_pv_power_site(resource_id: str, **kwargs) -> Response:
    """
    Delete an existing PV power site.

    Args:
        resource_id: unique string to identify the location that is generated when creating a site
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(base_url=base_url, endpoint=pv_power_site, response_type=Response)

    params = {"resource_id": resource_id, "format": "json", **kwargs}

    res = client.delete(params)

    return res
