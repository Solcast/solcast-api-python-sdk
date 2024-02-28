# PV Power Sites
Allows management of detailed PV power site metadata used by the `advanced_pv_power` functions.  More information is in the [API docs](https://docs.solcast.com.au/#49090b36-66db-4d0f-89d5-87d19f00bec1).

The module `pv_power_sites` has 6 functions available. Use the `res.to_dict()` method to see the site metadata.

| <div style="width:150px">Endpoint</div> | Purpose | API Docs |
|------|------|------|
| `list_pv_power_sites`     | List available PV power sites. | [details](https://docs.solcast.com.au/#baee4c8b-83e8-43e6-886b-98671164df10){.md-button} |
| `get_pv_power_site`       | Get an existing PV power site's specifications. | [details](https://docs.solcast.com.au/#27a18021-eed0-4281-8b28-9bdf1ebb2a95){.md-button} |
| `create_pv_power_site`     | Create PV power site to be used with Solcast's advanced PV power model. | [details](https://docs.solcast.com.au/#d3a35494-15d8-4baa-b96f-7fd3353c9f06){.md-button} |
| `patch_pv_power_site`     | Patch an existing PV power site to partially update the site's specifications. | [details](https://docs.solcast.com.au/#ba412164-31c2-47a9-a965-c95bc9b632a6){.md-button} |
| `update_pv_power_site`     | Overwrite an existing PV power site's specifications. | [details](https://docs.solcast.com.au/#181cf2be-f710-49c3-8050-07be858f25e1){.md-button} |
| `delete_pv_power_site`     | Delete an existing PV power site. | [details](https://docs.solcast.com.au/#c2353692-36db-46b8-8508-a6d4fae65390){.md-button} |

### Example

```python
from solcast import pv_power_sites

# Use pv_power_sites.list_pv_power_sites to find the resource_id
res = pv_power_sites.get_pv_power_site('ba75-e17a-7374-95ed')

res.to_dict()
```
```
{
    'resource_id': 'ba75-e17a-7374-95ed',  
    'name': 'Test Site: Sydney Opera House',  
    'latitude': -33.856784,  
    'longitude': 151.215297,  
    'capacity': 10,  
    'capacity_dc': 15,  
    'azimuth': 0,  
    'tilt': 30.22,  
    'tracking_type': 'horizontal_single_axis',  
    'install_date': '2021-07-01T00:00:00.0000000Z',  
    'module_type': 'poly-si',  
    'ground_coverage_ratio': 0.47,  
    'derating_temp_module': 0.0039,  
    'derating_age_system': 0.0059,  
    'derating_other_system': 0.07,  
    'inverter_peak_efficiency': 0.985,  
    'tracker_axis_azimuth': 0,  
    'tracker_max_rotation_angle': 60,  
    'tracker_back_tracking': True,  
    'tracker_smart_tracking': False,  
    'terrain_slope': 0,  
    'terrain_azimuth': 0,  
    'dust_soiling_average': [0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015,  
    0.015],  
    'bifacial_system': False,  
    'site_ground_albedo': 0.25,  
    'bifaciality_factor': 0.7,  
    'pvrow_height': 1.5,  
    'pvrow_width': 2,  
    'is_unmetered': True,  
    'confirmed_metadata': '2023-12-19T07:18:21.2378120Z'
 }
```
