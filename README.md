<img src="https://github.com/Solcast/solcast-api-python-sdk/blob/main/docs/img/logo.png?raw=true" width="100" align="right">

# Solcast API Python SDK

<em>Python SDK to access the Solcast API</em>

[![Docs](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/docs.yml/badge.svg)](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/docs.yml) [![Tests](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/test.yml) [![Publish 📦 to PyPI](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/Solcast/solcast-api-python-sdk/actions/workflows/publish-to-pypi.yml)

---

**Documentation**: <a href="https://solcast.github.io/solcast-api-python-sdk/" target="_blank">https://solcast.github.io/solcast-api-python-sdk/ </a>

## Install
```commandline
pip install solcast
```
or from source: 
```commandline
git clone https://github.com/Solcast/solcast-api-python-sdk.git
cd solcast-api-python-sdk
pip install .
```

The vanilla version doesn't have any dependency. For full functionality,
for example for getting the data into `DataFrames`, and for development, use the `[all]` tag: 
```commandline
pip install .[all] for the dev libs
```

## Basic Usage

```python
from solcast import live

df = live.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    output_parameters=['air_temp', 'dni', 'ghi']
).to_pandas()
```

Don't forget to set your [account Api Key](https://toolkit.solcast.com.au/register) with: 
```export SOLCAST_API_KEY={your commercial api_key}```

---

## Contributing
Tests are run against the Solcast API, you will need an API key to run them. 
They are executed on `unmetered locations` and as such won't consume your requests.

```commandline
pytest tests
```
