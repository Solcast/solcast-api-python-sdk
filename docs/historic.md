# Historic

Historical irradiance, weather and power data, from 2007 to 7 days ago at 1-2km and 5 minutes resolution.
For more information see the [API Docs](https://docs.solcast.com.au/#36bffd5d-d2b5-4bc3-b757-855624432375). 
The `Historic` module has 3 methods:

| Endpoint                | API Docs                                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| `radiation_and_weather` | [list of API parameters](https://docs.solcast.com.au/#9de907e7-a52f-4993-a0f0-5cffee78ad10){.md-button} |
| `rooftop_pv_power`      | [list of API parameters](https://docs.solcast.com.au/#504e6e52-992f-4ac2-a4dc-d7ab312f992a){.md-button}                |
| `advanced_pv_power`     | [list of API parameters](https://docs.solcast.com.au/#1db1132e-8d49-4f25-939f-34883e5336c4){.md-button}               |

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


## Example of multi period request for the year of 2023 from Jan 01
### The below code is using an unmetered location. If using a metered location, it will consume 12 request.

```python
from solcast import historic
import pandas as pd
from solcast.unmetered_locations import UNMETERED_LOCATIONS
from solcast import historic

site = UNMETERED_LOCATIONS["Stonehenge"]
latitude, longitude = site["latitude"], site["longitude"]

data = []
start_date = '2023-01-01'
start_dates = pd.date_range(start=start_date, periods=12, freq='MS')

for start in start_dates:
    start_str = start.strftime('%Y-%m-%dT00:00:00.000Z')
    end_date =  (start + pd.offsets.MonthEnd(1)).strftime('%Y-%m-%dT23:59:59.000Z')
    
    res = historic.radiation_and_weather(latitude=latitude, longitude=longitude, start=start_str, end=end_date)
    if res.success:
        data.append(res.to_pandas())
    else:
        print(res.exception)

output = pd.concat(data)
```