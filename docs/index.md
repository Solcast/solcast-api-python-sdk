# Welcome to Solcast
A simple Python SDK that wraps [Solcast's API](https://docs.solcast.com.au/). 

## Install
From the directory run the following command:
```bash 
pip install --user solcast
```
!!! tip

    for full functionality install **all**: `pip install --user solcast[all]`

## Usage
!!! warning 

    To access Solcast data you will need a [commercial API key](https://toolkit.solcast.com.au/register). If you have the API key already,
    you can use it with this library either as an environment variable called SOLCAST_API_KEY,
    or you can pass it as an argument `api_key` when you call one of the library's methods. 

Fetching live radiation and weather data:

```py
from solcast import live

res = live.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    output_parameters=['air_temp', 'dni', 'ghi']
)
```

!!! tip

    When testing or developing, you should use `solcast.unmetered_locations` so that your usage isn't counted against your plan.
   [Unmetered Locations](https://docs.solcast.com.au/#unmetered-locations) still require you to signup for a commercial API key (above).

```py
from solcast import forecast
from solcast.unmetered_locations import UNMETERED_LOCATIONS
sydney = UNMETERED_LOCATIONS['Sydney Opera House']

res = forecast.rooftop_pv_power(
    latitude=sydney['latitude'], 
    longitude=sydney['longitude'],
    period='PT5M',
    capacity=5,  # 5KW
    tilt=22,  # degrees
    output_parameters='pv_power_rooftop'
)
```


Where the data returned is a timeseries, the response can be converted to a Pandas DataFrame as follows.  This is available for all the modules apart from `pv_power_sites`.

```python
df = res.to_pandas()
```
!!! info
    Pandas is not installed by default to keep the environment light. It is installed with the [all] tag

For all the modules, data can be extracted in Python dictionary format.
```python
df = res.to_dict()
```


Available modules are 

| Module       | API Docs                        |
|--------------|---------------------------------|
| `live`       | [solcast.live](live.md)           |
| `historic` | [solcast.historic](historic.md) |
| `forecast`   | [solcast.forecast](forecast.md)   |
| `tmy`        | [solcast.tmy](tmy.md)             |
| `pv_power_sites` | [solcast.pv_power_sites](pv_power_sites) |


## Docs
from the directory run
```bash 
mkdocs build
mkdocs serve
```
In a browser navigate to `localhost:8000` to see the documentation.

## Contributing & License
Any type of suggestion and code contribution is welcome as PRs and/or Issues.
This repository is licensed under MIT (see LICENSE).
