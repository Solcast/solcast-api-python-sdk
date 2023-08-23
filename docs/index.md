# Welcome to SolPy
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

    To access Solcast data you will need an API key. If you have the API key already,
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

as a Pandas DataFrame

```python
df = res.to_pandas()
```
!!! info
    Pandas is not installed by default to keep the environment light. It is installed with the [all] tag


Available modules are 

| Method       | API Docs                        |
|--------------|---------------------------------|
| `live`       | [solpy.live](live.md)           |
| `historical` | [solpy.historical](historic.md) |
| `forecast`   | [solpy.forecast](forecast.md)   |
| `tmy`        | [solpy.tmy](tmy.md)             |


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
