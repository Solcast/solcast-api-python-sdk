# Historic

Historical irradiance, weather and power data, from 2007 to 7 days ago at 1-2km and 5 minutes resolution.
For more information see the [API Docs](https://docs.solcast.com.au/#36bffd5d-d2b5-4bc3-b757-855624432375). 
The `Historic` module has 3 methods:

| Endpoint                | API Docs                                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| `radiation_and_weather` | [list of API parameters](https://docs.solcast.com.au/#9de907e7-a52f-4993-a0f0-5cffee78ad10){.md-button} |
| `rooftop_pv_power`      | [list of API parameters](https://docs.solcast.com.au/#504e6e52-992f-4ac2-a4dc-d7ab312f992a){.md-button}                |
| `advanced_pv_power`     | [list of API parameters](https://docs.solcast.com.au/#1db1132e-8d49-4f25-939f-34883e5336c4){.md-button}               |

## Example of single-period request

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


## Example of 12 month combined multi-period requests
The below code is using an unmetered location. If using a metered location, it will consume 12 requests.
For more information see the [API Docs](https://solcast.github.io/solcast-api-python-sdk/notebooks/1.3%20Getting%20Data%20-%20Make%20Concurrent%20Requests/). 

```python
import time
import pandas as pd
from solcast import historic
from solcast.unmetered_locations import UNMETERED_LOCATIONS

sydney = UNMETERED_LOCATIONS['Sydney Opera House']
data = []
start_date = '2023-01-01'
start_dates = pd.date_range(start=start_date, periods=12, freq='MS')

for start_day in start_dates:
    end_day = (start_day + pd.offsets.MonthEnd(1)).strftime('%Y-%m-%dT23:59:59.000Z')
    
    try:
        res = historic.radiation_and_weather(
            latitude=sydney['latitude'],
            longitude=sydney['longitude'],
            start=start_day,
            end=end_day,
        )
        data.append(res.to_pandas())
    except Exception as e:
        print(f"Request failed for start date {start_day}: {e}")
    
    # Delay between requests to avoid hitting the default historic rate limit
    time.sleep(1) 

data = pd.concat(data)
data
```

| period_end                |   air_temp |   dni |   ghi |
|:--------------------------|-----------:|------:|------:|
| 2023-01-01 00:30:00+00:00 |         22 |   819 |   917 |
| 2023-01-01 01:00:00+00:00 |         23 |   924 |   996 |
| 2023-01-01 01:30:00+00:00 |         23 |   935 |  1028 |
| 2023-01-01 02:00:00+00:00 |         23 |   761 |   977 |
| 2023-01-01 02:30:00+00:00 |         23 |   702 |   953 |
...                             ...  ...   ...
| 2023-12-31 22:00:00+00:00 |         21 |   329 |   435 |
| 2023-12-31 22:30:00+00:00 |         21 |     0 |   273 |
| 2023-12-31 23:00:00+00:00 |         21 |     0 |   330 |
| 2023-12-31 23:30:00+00:00 |         22 |     0 |   349 |
| 2024-01-01 00:00:00+00:00 |         22 |     0 |   324 |