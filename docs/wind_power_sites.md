# Wind Power Sites

Manage Premium Wind power site resources.

| Method | Purpose | API Docs |
|---|---|---|
| `list_wind_power_sites` | List accessible sites, with optional search and filters. | [details](https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSites) |
| `get_wind_power_site` | Retrieve a site by resource ID. | [details](https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSite) |
| `create_wind_power_site` | Create a site. Name, coordinates, and capacity are required. | [details](https://docs.solcast.com.au/docs/section/premium#postResourcesWindPowerSite) |
| `patch_wind_power_site` | Partially update fields supplied in the request. | [details](https://docs.solcast.com.au/docs/section/premium#patchResourcesWindPowerSite) |
| `update_wind_power_site` | Replace a site definition. Resource ID, name, coordinates, and capacity are required. | [details](https://docs.solcast.com.au/docs/section/premium#putResourcesWindPowerSite) |
| `delete_wind_power_site` | Delete a site by resource ID. | [details](https://docs.solcast.com.au/docs/section/premium#deleteResourcesWindPowerSite) |

## List and retrieve

```python
from solcast import wind_power_sites

res = wind_power_sites.list_wind_power_sites(query="Sydney")
sites = res.to_dict()["results"]

site = wind_power_sites.get_wind_power_site(
    resource_id="your-wind-resource-id",
)
site.to_dict()
```

## Create and update

Create a site with the required fields and any optional turbine settings:

```python
res = wind_power_sites.create_wind_power_site(
    name="Example wind site",
    latitude=-33.8567,
    longitude=151.2152,
    capacity=5,
    rotor_diameter=120,
    hub_height=100,
    number_of_turbines=2,
)
resource_id = res.to_dict()["resource_id"]
```

PATCH changes only the fields supplied. PUT replaces the definition and requires the full set of required fields:

```python
wind_power_sites.patch_wind_power_site(
    resource_id=resource_id,
    allow_negative_power=True,
)

wind_power_sites.update_wind_power_site(
    resource_id=resource_id,
    name="Example wind site",
    latitude=-33.8567,
    longitude=151.2152,
    capacity=5,
    rotor_diameter=120,
    hub_height=100,
    number_of_turbines=2,
)
```

## Delete

```python
wind_power_sites.delete_wind_power_site(resource_id=resource_id)
```

Each method returns the SDK `Response` object. Use `response.to_dict()` to inspect the JSON response.