import json
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

import pandas as pd

from solcast import pv_power_site_measurements, wind_power_site_measurements


class FakeResponse:
    code = 200

    def __init__(self, body=b'{"accepted": 1}'):
        self.body = body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return self.body


def capture_request(mock_urlopen):
    request = mock_urlopen.call_args.args[0]
    return request, urlsplit(request.full_url)


def test_create_pv_site_measurements_sends_json_body():
    measurements = [
        {
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 1.25,
        }
    ]

    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = pv_power_site_measurements.create_pv_site_measurements(
            resource_id="pv-123",
            measurements=measurements,
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert response.to_dict()["accepted"] == 1
    assert request.method == "POST"
    assert parsed_url.path == "/resources/pv_power_site_measurements"
    assert parse_qs(parsed_url.query) == {"format": ["json"]}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {
        "resource_id": "pv-123",
        "measurements": measurements,
    }


def test_create_pv_site_measurements_accepts_dataframe():
    measurements = pd.DataFrame(
        {
            "period_end": [pd.Timestamp("2026-01-01T00:30:00Z")],
            "period": ["PT30M"],
            "power": [1.25],
        }
    )

    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = pv_power_site_measurements.create_pv_site_measurements(
            resource_id="pv-123",
            measurements=measurements,
            api_key="test-key",
        )

    request, _ = capture_request(mock_urlopen)
    assert response.to_dict()["accepted"] == 1
    assert json.loads(request.data) == {
        "resource_id": "pv-123",
        "measurements": [
            {
                "period_end": "2026-01-01T00:30:00+00:00",
                "period": "PT30M",
                "power": 1.25,
            }
        ],
    }


def test_get_pv_site_measurements_pandas_preserves_page_metadata():
    response_body = {
        "offset": 10,
        "total": 12,
        "results": [
            {
                "period_end": "2026-01-01T00:30:00+00:00",
                "period": "PT30M",
                "power": 1.25,
            },
            {
                "period_end": "2026-01-01T01:00:00+00:00",
                "period": "PT30M",
                "power": 1.4,
            },
        ],
    }
    with patch(
        "solcast.api.urlopen",
        return_value=FakeResponse(json.dumps(response_body).encode("utf-8")),
    ):
        response = pv_power_site_measurements.get_pv_site_measurements(
            resource_id="pv-123",
            skip=10,
            take=2,
            api_key="test-key",
        )

    frame = response.to_pandas()
    assert frame["power"].tolist() == [1.25, 1.4]
    assert frame.index.tz is not None
    assert response.to_dict()["offset"] == 10
    assert response.to_dict()["total"] == 12


def test_get_pv_site_measurements_pandas_handles_empty_page():
    response_body = {"offset": 0, "total": 0, "results": []}
    with patch(
        "solcast.api.urlopen",
        return_value=FakeResponse(json.dumps(response_body).encode("utf-8")),
    ):
        response = pv_power_site_measurements.get_pv_site_measurements(
            resource_id="pv-123",
            api_key="test-key",
        )

    assert response.to_pandas().empty


def test_get_pv_sub_unit_measurements_sends_filters_as_query():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = pv_power_site_measurements.get_pv_sub_unit_measurements(
            resource_id="pv-123",
            sub_unit="inverter-1",
            start="2026-01-01T00:00:00Z",
            end="2026-01-02T00:00:00Z",
            skip=20,
            take=50,
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "GET"
    assert parsed_url.path == "/resources/pv_power_site_measurements/sub_units"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["pv-123"],
        "sub_unit": ["inverter-1"],
        "start": ["2026-01-01T00:00:00Z"],
        "end": ["2026-01-02T00:00:00Z"],
        "skip": ["20"],
        "take": ["50"],
        "format": ["json"],
    }


def test_delete_wind_site_measurements_sends_required_time_bounds():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_site_measurements.delete_wind_site_measurements(
            resource_id="wind-123",
            start="2026-01-01T00:00:00Z",
            end="2026-01-02T00:00:00Z",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "DELETE"
    assert parsed_url.path == "/resources/wind_power_site_measurements"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["wind-123"],
        "start": ["2026-01-01T00:00:00Z"],
        "end": ["2026-01-02T00:00:00Z"],
        "format": ["json"],
    }


def test_create_wind_sub_unit_measurements_sends_json_body():
    measurements = [
        {
            "sub_unit": "turbine-1",
            "period_end": "2026-01-01T00:30:00Z",
            "period": "PT30M",
            "power": 2.5,
            "wind_speed_hub_height": 8.2,
        }
    ]

    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_site_measurements.create_wind_sub_unit_measurements(
            resource_id="wind-123",
            measurements=measurements,
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert response.to_dict()["accepted"] == 1
    assert request.method == "POST"
    assert parsed_url.path == "/resources/wind_power_site_measurements/sub_units"
    assert parse_qs(parsed_url.query) == {"format": ["json"]}
    assert json.loads(request.data) == {
        "resource_id": "wind-123",
        "measurements": measurements,
    }


def test_measurement_modules_expose_all_site_and_sub_unit_operations():
    expected_pv_names = {
        "create_pv_site_measurements",
        "get_pv_site_measurements",
        "delete_pv_site_measurements",
        "create_pv_sub_unit_measurements",
        "get_pv_sub_unit_measurements",
        "delete_pv_sub_unit_measurements",
    }
    expected_wind_names = {
        "create_wind_site_measurements",
        "get_wind_site_measurements",
        "delete_wind_site_measurements",
        "create_wind_sub_unit_measurements",
        "get_wind_sub_unit_measurements",
        "delete_wind_sub_unit_measurements",
    }

    assert expected_pv_names.issubset(vars(pv_power_site_measurements))
    assert expected_wind_names.issubset(vars(wind_power_site_measurements))
