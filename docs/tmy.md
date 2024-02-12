# TMY

TMY (Typical Meteorological Year) is a collation of historical weather data for a specified location for a one year period. 
The dataset is derived from a multi-year time series specifically selected so that it presents the unique weather 
phenomena for the location, and provides annual averages that are consistent with long term averages.
See the [API docs](https://docs.solcast.com.au/#2144b738-a1f7-4647-9067-6e7f6eca32a8)
The `tmy` module has 2 methods:

| Endpoint                | API Docs                                                                                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `radiation_and_weather` | [details](https://docs.solcast.com.au/?#e75039fa-86ec-43e4-99a3-389d3d7a4a99){.md-button}  |
| `rooftop_pv_power`      | [details](https://docs.solcast.com.au/?#d117fde9-e410-4df0-bd07-e6168efd23cf){.md-button}  |

### Example

```python
from solcast import tmy

res = tmy.rooftop_pv_power(
    latitude=-33.856784,
    longitude=151.215297,
    capacity=3
)

res.to_pandas().head()
``` 

| period_end                |   pv_power_rooftop |
|:--------------------------|-------------------:|
| 2059-01-01 01:00:00+00:00 |              1.461 |
| 2059-01-01 02:00:00+00:00 |              0.974 |
| 2059-01-01 03:00:00+00:00 |              0.731 |
| 2059-01-01 04:00:00+00:00 |              0.4   |
| 2059-01-01 05:00:00+00:00 |              0.231 |
