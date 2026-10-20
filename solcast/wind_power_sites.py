from .api import Client, Response
from .urls import base_url, wind_power_site, wind_power_sites


def create_wind_power_site(
    name: str, latitude: float, longitude: float, capacity: float, **kwargs
) -> Response:
    """
    Create Resource

    Args:
        name: The name of the resource.
        latitude: The latitude of the resource. Must be a decimal number between -90 and 90.
        longitude: The longitude of the resource. Must be a decimal number between -180 and 180.
        capacity: The site capacity (rated power × number of turbines) in MW.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#postResourcesWindPowerSite.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_site,
        response_type=Response,
    )

    request_body = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "capacity": capacity,
    }
    body_value = kwargs.pop("rotor_diameter", None)
    if body_value is not None:
        request_body["rotor_diameter"] = body_value
    body_value = kwargs.pop("rated_power", None)
    if body_value is not None:
        request_body["rated_power"] = body_value
    body_value = kwargs.pop("hub_height", None)
    if body_value is not None:
        request_body["hub_height"] = body_value
    body_value = kwargs.pop("number_of_turbines", None)
    if body_value is not None:
        request_body["number_of_turbines"] = body_value
    body_value = kwargs.pop("cut_in_wind_speed", None)
    if body_value is not None:
        request_body["cut_in_wind_speed"] = body_value
    body_value = kwargs.pop("cut_out_wind_speed", None)
    if body_value is not None:
        request_body["cut_out_wind_speed"] = body_value
    body_value = kwargs.pop("rated_wind_speed", None)
    if body_value is not None:
        request_body["rated_wind_speed"] = body_value
    body_value = kwargs.pop("allow_negative_power", None)
    if body_value is not None:
        request_body["allow_negative_power"] = body_value
    body_value = kwargs.pop("grid_export_limit", None)
    if body_value is not None:
        request_body["grid_export_limit"] = body_value
    return client.post(
        {**kwargs},
        json_body=request_body,
    )


def delete_wind_power_site(resource_id: str, **kwargs) -> Response:
    """
    Delete a premium wind power site.

    Args:
        resource_id: The unique identifier of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#deleteResourcesWindPowerSite.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_site,
        response_type=Response,
    )

    return client.delete({"resource_id": resource_id, **kwargs})


def get_wind_power_site(resource_id: str, **kwargs) -> Response:
    """
    Retrieve details of a specific premium wind power site.

    Args:
        resource_id: The unique identifier of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSite.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_site,
        response_type=Response,
    )

    return client.get({"resource_id": resource_id, "format": "json", **kwargs})


def list_wind_power_sites(**kwargs) -> Response:
    """
    Lists all premium wind power sites accessible to the authenticated user.

    Args:
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSites.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_sites,
        response_type=Response,
    )

    return client.get({"format": "json", **kwargs})


def patch_wind_power_site(resource_id: str, **kwargs) -> Response:
    """
    Patch Resource

    Args:
        resource_id: The unique identifier of the resource.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#patchResourcesWindPowerSite.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_site,
        response_type=Response,
    )

    request_body = {
        "resource_id": resource_id,
    }
    body_value = kwargs.pop("rotor_diameter", None)
    if body_value is not None:
        request_body["rotor_diameter"] = body_value
    body_value = kwargs.pop("rated_power", None)
    if body_value is not None:
        request_body["rated_power"] = body_value
    body_value = kwargs.pop("hub_height", None)
    if body_value is not None:
        request_body["hub_height"] = body_value
    body_value = kwargs.pop("number_of_turbines", None)
    if body_value is not None:
        request_body["number_of_turbines"] = body_value
    body_value = kwargs.pop("cut_in_wind_speed", None)
    if body_value is not None:
        request_body["cut_in_wind_speed"] = body_value
    body_value = kwargs.pop("cut_out_wind_speed", None)
    if body_value is not None:
        request_body["cut_out_wind_speed"] = body_value
    body_value = kwargs.pop("rated_wind_speed", None)
    if body_value is not None:
        request_body["rated_wind_speed"] = body_value
    body_value = kwargs.pop("allow_negative_power", None)
    if body_value is not None:
        request_body["allow_negative_power"] = body_value
    body_value = kwargs.pop("grid_export_limit", None)
    if body_value is not None:
        request_body["grid_export_limit"] = body_value
    return client.patch(
        {**kwargs},
        json_body=request_body,
    )


def update_wind_power_site(
    resource_id: str,
    name: str,
    latitude: float,
    longitude: float,
    capacity: float,
    **kwargs,
) -> Response:
    """
    Update Resource

    Args:
        resource_id: The unique identifier of the resource.
        name: The name of the resource.
        latitude: The latitude of the resource. Must be a decimal number between -90 and 90.
        longitude: The longitude of the resource. Must be a decimal number between -180 and 180.
        capacity: The site capacity (rated power × number of turbines) in MW.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/docs/section/premium#putResourcesWindPowerSite.
    """
    url = kwargs.pop("base_url", base_url)

    client = Client(
        base_url=url,
        endpoint=wind_power_site,
        response_type=Response,
    )

    request_body = {
        "resource_id": resource_id,
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "capacity": capacity,
    }
    body_value = kwargs.pop("rotor_diameter", None)
    if body_value is not None:
        request_body["rotor_diameter"] = body_value
    body_value = kwargs.pop("rated_power", None)
    if body_value is not None:
        request_body["rated_power"] = body_value
    body_value = kwargs.pop("hub_height", None)
    if body_value is not None:
        request_body["hub_height"] = body_value
    body_value = kwargs.pop("number_of_turbines", None)
    if body_value is not None:
        request_body["number_of_turbines"] = body_value
    body_value = kwargs.pop("cut_in_wind_speed", None)
    if body_value is not None:
        request_body["cut_in_wind_speed"] = body_value
    body_value = kwargs.pop("cut_out_wind_speed", None)
    if body_value is not None:
        request_body["cut_out_wind_speed"] = body_value
    body_value = kwargs.pop("rated_wind_speed", None)
    if body_value is not None:
        request_body["rated_wind_speed"] = body_value
    body_value = kwargs.pop("allow_negative_power", None)
    if body_value is not None:
        request_body["allow_negative_power"] = body_value
    body_value = kwargs.pop("grid_export_limit", None)
    if body_value is not None:
        request_body["grid_export_limit"] = body_value
    return client.put(
        {**kwargs},
        json_body=request_body,
    )
