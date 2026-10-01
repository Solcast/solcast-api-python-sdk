import subprocess
import sys
from pathlib import Path

import pytest

from solcast.api import Client, PandafiableResponse, Response
from solcast.urls import (
    _get_base_url,
    base_url,
    historic_radiation_and_weather,
    live_radiation_and_weather,
)


@pytest.fixture
def mock_short_key(monkeypatch):
    monkeypatch.setenv("SOLCAST_API_KEY", "")


@pytest.mark.parametrize(
    ("configured_url", "expected_url"),
    [
        ("https://example.test/", "https://example.test"),
        ("http://localhost:8080/", "http://localhost:8080"),
    ],
)
def test_base_url_normalizes_configured_url(monkeypatch, configured_url, expected_url):
    monkeypatch.setenv("SOLCAST_API_BASE_URL", configured_url)

    assert _get_base_url() == expected_url


@pytest.mark.parametrize(
    "configured_url",
    [
        "https://*.example.test",
        "ftp://example.test",
        "https:///path",
        "https://example.test?environment=dev",
        "https://example.test#fragment",
    ],
)
def test_base_url_rejects_invalid_url(monkeypatch, configured_url):
    monkeypatch.setenv("SOLCAST_API_BASE_URL", configured_url)

    with pytest.raises(ValueError, match="absolute HTTP"):
        _get_base_url()


def test_base_url_defaults_to_production(monkeypatch):
    monkeypatch.delenv("SOLCAST_API_BASE_URL", raising=False)

    assert _get_base_url() == "https://api.solcast.com.au"


def test_configured_base_url_is_shared_by_endpoint_modules(monkeypatch):
    monkeypatch.setenv("SOLCAST_API_BASE_URL", "https://example.test")
    code = """
import solcast

modules = (
    solcast.aggregations,
    solcast.forecast,
    solcast.historic,
    solcast.live,
    solcast.pv_power_sites,
    solcast.pv_power_site_measurements,
    solcast.wind_power_site_measurements,
    solcast.tmy,
)
assert all(module.base_url == "https://example.test" for module in modules)
"""

    subprocess.run(
        [sys.executable, "-c", code],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
    )


def test_fail_short_key(mock_short_key):
    with pytest.raises(ValueError, match="API key is too short."):
        cls = Client(
            base_url=base_url,
            endpoint=live_radiation_and_weather,
            response_type=PandafiableResponse,
        )
        cls._check_params({"a": None})


def test_pass_key_in_params(mock_short_key):
    cls = Client(
        base_url=base_url,
        endpoint=live_radiation_and_weather,
        response_type=PandafiableResponse,
    )
    assert cls._check_params({"api_key": "dummy"})[1] == "dummy"


def test_client():
    cli = Client(
        base_url=base_url,
        endpoint=live_radiation_and_weather,
        response_type=PandafiableResponse,
    )
    assert cli.url.startswith("https")

    res = cli.get(
        {
            "latitude": -33.856784,
            "longitude": 151.215297,
            "output_parameters": "ghi",
            "hours": 1,
            "format": "json",
        }
    )

    assert res.code == 200
    assert len(res.to_dict()) == 1

    params, _ = cli._check_params(
        {
            "latitude": -33.8567848776324,
            "longitude": 151.215297,
            "output_parameters": "ghi",
            "hours": 1,
            "format": "json",
        }
    )

    assert params["latitude"] == -33.856785


def test_response():
    raw_data = b'{"estimated_actuals":[{"ghi":54,"period_end":"2023-06-22T05:30:00.0000000Z","period":"PT30M"}]}'
    rsp = Response(
        data=raw_data, url="some_url", code=200, success=True, method="arbitrary_method"
    )

    assert rsp.success is True


def test_pandafiable_response():
    raw_data = b'{"estimated_actuals":[{"ghi":54,"period_end":"2023-06-22T05:30:00.0000000Z","period":"PT30M"}]}'
    rsp = PandafiableResponse(
        data=raw_data, url="some_url", code=200, success=True, method="arbitrary_method"
    )

    assert rsp.success is True
    assert rsp.to_pandas().shape[0] == 1


def test_timezone():
    cli = Client(
        base_url=base_url,
        endpoint=historic_radiation_and_weather,
        response_type=PandafiableResponse,
    )
    res = cli.get(
        {
            "latitude": -33.856784,
            "longitude": 151.215297,
            "output_parameters": "air_temp",
            "start": "2022-10-25T14:45:00.000Z",
            "duration": "P1D",
            "format": "json",
        }
    )

    assert res.to_pandas().index.tz is not None
