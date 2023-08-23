# Historic

Historical irradiance, weather and power data, from 2007 to 7 days ago at 1-2km and 5 minutes resolution.
For more information see the [API Docs](https://docs.solcast.com.au/#36bffd5d-d2b5-4bc3-b757-855624432375). 
The `Historic` module has 2 methods:

| Endpoint                | API Docs                                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| `radiation_and_weather` | [list of API parameters](https://docs.solcast.com.au/#9de907e7-a52f-4993-a0f0-5cffee78ad10){.md-button} |
| `rooftop_pv_power`      | [list of API parameters](https://docs.solcast.com.au/#504e6e52-992f-4ac2-a4dc-d7ab312f992a){.md-button}                |

### Example

```python
from solcast import historic

res = historic.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    start='2022-06-01T06:00',
    duration='P1D'
)

res.to_pandas().head()
```

| period_end                |   air_temp |   dni |   ghi |
|:--------------------------|-----------:|------:|------:|
| 2022-06-01 06:30:00+00:00 |         13 |   441 |    78 |
| 2022-06-01 07:00:00+00:00 |         13 |    62 |    12 |
| 2022-06-01 07:30:00+00:00 |         13 |     0 |     0 |
| 2022-06-01 08:00:00+00:00 |         12 |     0 |     0 |
| 2022-06-01 08:30:00+00:00 |         12 |     0 |     0 |