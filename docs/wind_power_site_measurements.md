# Premium Wind Site Measurements

The `wind_power_site_measurements` module manages measured power data for Premium Wind Power sites.

All measurement records use ISO-8601 timestamps. Site measurement power is measured in MW.

`pandas` is optional. DataFrame uploads and `to_pandas()` need it. Install it with `pip install pandas` or `pip install 'solcast[all]'`; list uploads and `to_dict()` do not need pandas.

See the Premium API schemas for [site upload](https://docs.solcast.com.au/docs/section/premium#postResourcesWindPowerSiteMeasurements), [site retrieval](https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSiteMeasurements), and [site deletion](https://docs.solcast.com.au/docs/section/premium#deleteResourcesWindPowerSiteMeasurements). For sub-unit data, see [sub-unit upload](https://docs.solcast.com.au/docs/section/premium#postResourcesWindPowerSiteMeasurementsSubUnits), [sub-unit retrieval](https://docs.solcast.com.au/docs/section/premium#getResourcesWindPowerSiteMeasurementsSubUnits), and [sub-unit deletion](https://docs.solcast.com.au/docs/section/premium#deleteResourcesWindPowerSiteMeasurementsSubUnits).

| Method | Purpose |
|---|---|
| `create_wind_site_measurements` | Submit site measurements. |
| `get_wind_site_measurements` | Retrieve site measurements, with optional `start` and `end` filters. |
| `delete_wind_site_measurements` | Delete site measurements between required `start` and `end` timestamps. |
| `create_wind_sub_unit_measurements` | Submit measurements for labelled site sub-units. |
| `get_wind_sub_unit_measurements` | Retrieve sub-unit measurements, optionally filtered by `sub_unit`, `start`, and `end`. |
| `delete_wind_sub_unit_measurements` | Delete sub-unit measurements between required `start` and `end` timestamps. |

## Create site measurements

```python
import pandas as pd
from solcast import wind_power_site_measurements

measurements = pd.DataFrame(
    [
        {
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 2.5,
            "wind_speed_hub_height": 8.2,
            "wind_direction_hub_height": 180,
        }
    ]
)

response = wind_power_site_measurements.create_wind_site_measurements(
    resource_id="your-premium-wind-site",
    measurements=measurements,
)
```

Create sub-unit measurements with a `sub_unit` value on every record:

```python
response = wind_power_site_measurements.create_wind_sub_unit_measurements(
    resource_id="your-premium-wind-site",
    measurements=[
        {
            "sub_unit": "turbine-1",
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 2.5,
            "wind_speed_hub_height": 8.2,
        }
    ],
)
```

## Upload and download large datasets

Each create request accepts up to 1,000 measurements. Split a DataFrame into batches with `.iloc` and check each response:

```python
# measurements is the complete list of records to upload.
for start_index in range(0, len(measurements), 1000):
    batch = measurements.iloc[start_index : start_index + 1000]
    response = wind_power_site_measurements.create_wind_site_measurements(
        resource_id="your-premium-wind-site",
        measurements=batch,
        format="json",
    )
    if not response.success:
        raise RuntimeError(response.exception)
    print(f"Accepted {response.to_dict()['accepted']} measurements")
```

For a list of sub-unit records, use ordinary list slicing instead of `.iloc`. Include a `sub_unit` label in each record and use `create_wind_sub_unit_measurements`.

Retrieve all matching records with `skip` and `take`. This example requests 100 records per page. Use `to_dict()` for pagination metadata and `to_pandas()` for each page:

```python
import pandas as pd

measurement_pages = []
skip = 0
take = 100

while True:
    response = wind_power_site_measurements.get_wind_site_measurements(
        resource_id="your-premium-wind-site",
        start="2026-01-01T00:00:00Z",
        end="2026-02-01T00:00:00Z",
        skip=skip,
        take=take,
    )
    if not response.success:
        raise RuntimeError(response.exception)

    page = response.to_dict()
    page_frame = response.to_pandas()
    if not page_frame.empty:
        measurement_pages.append(page_frame)

    skip = page["offset"] + len(page_frame)
    if page_frame.empty or skip >= page["total"]:
        break

if measurement_pages:
    all_measurements = pd.concat(measurement_pages)
    display(all_measurements)
else:
    print("No measurements found.")
```

For sub-unit data, use `get_wind_sub_unit_measurements` with the same `skip` and `take` parameters. Add `sub_unit` to filter to one turbine.

All methods return the SDK `Response` object. GET responses also support `to_pandas()` for the current page of measurement data.
