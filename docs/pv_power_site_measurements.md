# Premium PV Site Measurements

The `pv_power_site_measurements` module manages measured power data for Premium PV Power sites.

All measurement records use ISO-8601 timestamps. Site measurement power is measured in MW.

See the Premium API schemas for [site upload](https://docs.solcast.com.au/docs/section/premium#postResourcesPvPowerSiteMeasurements), [site retrieval](https://docs.solcast.com.au/docs/section/premium#getResourcesPvPowerSiteMeasurements), and [site deletion](https://docs.solcast.com.au/docs/section/premium#deleteResourcesPvPowerSiteMeasurements). For sub-unit data, see [sub-unit upload](https://docs.solcast.com.au/docs/section/premium#postResourcesPvPowerSiteMeasurementsSubUnits), [sub-unit retrieval](https://docs.solcast.com.au/docs/section/premium#getResourcesPvPowerSiteMeasurementsSubUnits), and [sub-unit deletion](https://docs.solcast.com.au/docs/section/premium#deleteResourcesPvPowerSiteMeasurementsSubUnits).

| Method | Purpose |
|---|---|
| `create_pv_site_measurements` | Submit site measurements. |
| `get_pv_site_measurements` | Retrieve site measurements, with optional `start` and `end` filters. |
| `delete_pv_site_measurements` | Delete site measurements between required `start` and `end` timestamps. |
| `create_pv_sub_unit_measurements` | Submit measurements for labelled site sub-units. |
| `get_pv_sub_unit_measurements` | Retrieve sub-unit measurements, optionally filtered by `sub_unit`, `start`, and `end`. |
| `delete_pv_sub_unit_measurements` | Delete sub-unit measurements between required `start` and `end` timestamps. |

## Create site measurements

```python
from solcast import pv_power_site_measurements

response = pv_power_site_measurements.create_pv_site_measurements(
    resource_id="your-premium-pv-site",
    measurements=[
        {
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 1.25,
        }
    ],
)
```

Create sub-unit measurements with a `sub_unit` value on every record:

```python
response = pv_power_site_measurements.create_pv_sub_unit_measurements(
    resource_id="your-premium-pv-site",
    measurements=[
        {
            "sub_unit": "inverter-1",
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 1.25,
        }
    ],
)
```

## Upload and download large datasets

Each create request accepts up to 1,000 measurements. Split larger lists into batches and check each response:

```python
# measurements is the complete list of records to upload.
for start_index in range(0, len(measurements), 1000):
    batch = measurements[start_index : start_index + 1000]
    response = pv_power_site_measurements.create_pv_site_measurements(
        resource_id="your-premium-pv-site",
        measurements=batch,
        format="json",
    )
    if not response.success:
        raise RuntimeError(response.exception)
    print(f"Accepted {response.to_dict()['accepted']} measurements")
```

Use the same batching pattern with `create_pv_sub_unit_measurements`; include a `sub_unit` label in each record.

Retrieve all matching records with `skip` and `take`. This example requests 100 records per page. The response has `offset`, `total`, and `results` fields:

```python
all_measurements = []
skip = 0
take = 100

while True:
    response = pv_power_site_measurements.get_pv_site_measurements(
        resource_id="your-premium-pv-site",
        start="2026-01-01T00:00:00Z",
        end="2026-02-01T00:00:00Z",
        skip=skip,
        take=take,
    )
    if not response.success:
        raise RuntimeError(response.exception)

    page = response.to_dict()
    records = page["results"]
    all_measurements.extend(records)
    skip = page["offset"] + len(records)
    if not records or skip >= page["total"]:
        break
```

For sub-unit data, use `get_pv_sub_unit_measurements` with the same `skip` and `take` parameters. Add `sub_unit` to filter to one inverter.

All methods return the SDK `Response` object. Use `response.to_dict()` to inspect the JSON response.
