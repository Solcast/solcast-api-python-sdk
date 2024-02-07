# PV Power Sites
Allows management of detailed PV power site metadata used by the `advanced_pv_power` endpoints.  Sites are identified via their `resource_id` string.  More information is in the [API docs](https://docs.solcast.com.au/#49090b36-66db-4d0f-89d5-87d19f00bec1).

The module `pv_power_sites` has 6 available functions.

| Endpoint | Purpose | API Docs |
|------|------|------|
| `list_pv_power_sites` | List available PV power sites. | [details](https://docs.solcast.com.au/#baee4c8b-83e8-43e6-886b-98671164df10){.md-button} |
| `get_pv_power_site`      | Get an existing PV power site's specifications. | [details](https://docs.solcast.com.au/#27a18021-eed0-4281-8b28-9bdf1ebb2a95){.md-button} |
| `create_pv_power_site`     | Create PV power site to be used with Solcast's advanced PV power model. | [details](https://docs.solcast.com.au/#d3a35494-15d8-4baa-b96f-7fd3353c9f06){.md-button} |
| `patch_pv_power_site`     | Patch an existing PV power site to partially update the site's specifications. | [details](https://docs.solcast.com.au/#ba412164-31c2-47a9-a965-c95bc9b632a6){.md-button} |
| `update_pv_power_site`     | Overwrite an existing PV power site's specifications. | [details](https://docs.solcast.com.au/#181cf2be-f710-49c3-8050-07be858f25e1){.md-button} |
| `delete_pv_power_site`     | Delete an existing PV power site. | [details](https://docs.solcast.com.au/#c2353692-36db-46b8-8508-a6d4fae65390){.md-button} |

### Example

```python
from solcast import pv_power_sites

res = forecast.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    output_parameters='air_temp'
)

res.to_pandas().head()
```

| period_end                |   air_temp |
|:--------------------------|-----------:|
| 2023-08-18 04:00:00+00:00 |         16 |
| 2023-08-18 04:30:00+00:00 |         15 |
| 2023-08-18 05:00:00+00:00 |         15 |
| 2023-08-18 05:30:00+00:00 |         15 |
| 2023-08-18 06:00:00+00:00 |         15 |