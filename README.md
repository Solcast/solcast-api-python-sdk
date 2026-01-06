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

The base solcast sdk install requires only the python standard library.
Pandas is the only optional dependency that adds functionality to the package.

```commandline
pip install solcast pandas
```

The example notebooks use a variety of optional dependencies to showcase different
ways in which the Solcast API may be used. To install these dependencies run

```commandline
pip install solcast[all]
```


## Basic Usage

```python
from solcast import live

res = live.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    output_parameters=['air_temp', 'dni', 'ghi']
)
res.to_dict()
res.to_pandas()  # requires optional pandas installation
```

Don't forget to set your [account Api Key](https://toolkit.solcast.com.au/register) with:
`export SOLCAST_API_KEY={your commercial api_key}`

---

## Contributing

Tests are run against the Solcast API, you will need an API key to run them.
They are executed on `unmetered locations` and as such won't consume your requests.

```commandline
pytest tests
```

## Docs

From the directory run
```bash
mkdocs build
mkdocs serve
```
In a browser navigate to `localhost:8000` to see the documentation.

### Formatters and Linters

| Language | Formatter/Linter |
| -------- | ---------------- |
| `yaml`   | `yamlls`         |
| `toml`   | `taplo`          |
| `python` | `black`          |

### Recommended Python Development Version

Develop on the oldest supported `Python` version.

```bash
uv python pin 3.8
```
