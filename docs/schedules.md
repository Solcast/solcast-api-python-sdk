# Schedules

Retrieve and update availability or curtailment schedules for Premium PV and Wind resources.

| Method | Purpose | API Docs |
|---|---|---|
| `get_resource_schedule` | Retrieve schedule intervals for a time window. | [details](https://docs.solcast.com.au/docs/section/premium#getManageSchedules) |
| `patch_resource_schedule` | Merge availability and/or curtailment intervals into the schedule. | [details](https://docs.solcast.com.au/docs/section/premium#patchManageSchedules) |
| `delete_resource_schedule` | Remove schedule data for a time window and schedule type(s). | [details](https://docs.solcast.com.au/docs/section/premium#deleteManageSchedules) |

## Retrieve a schedule

```python
from solcast import schedules

response = schedules.get_resource_schedule(
    resource_id="your-premium-site",
    period_start="2026-01-01T00:00:00Z",
    period_end="2026-01-02T00:00:00Z",
)

data = response.to_dict()
```

## Patch schedule intervals

```python
response = schedules.patch_resource_schedule(
    resource_id="your-premium-site",
    availability_schedule=[
        {
            "period_start": "2026-01-01T00:00:00Z",
            "period_end": "2026-01-01T01:00:00Z",
            "availability": 75,
        }
    ],
)
```

## Delete schedule data

```python
response = schedules.delete_resource_schedule(
    resource_id="your-premium-site",
    period_start="2026-01-01T00:00:00Z",
    period_end="2026-01-02T00:00:00Z",
    schedule_type="availability,curtailment",
)
```

All methods return the SDK `Response` object. Use `response.to_dict()` to inspect the JSON response.