import json
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from solcast import wind_power_sites


class FakeResponse:
    code = 200

    def __init__(self, body=b'{"resource_id": "wind-123"}'):
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


def test_list_wind_power_sites_sends_filters_and_custom_base_url():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.list_wind_power_sites(
            show_all=False,
            query="Sydney",
            start="2026-01-01T00:00:00Z",
            end="2026-02-01T00:00:00Z",
            forecast_production=True,
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "GET"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_sites"
    assert parse_qs(parsed_url.query) == {
        "show_all": ["False"],
        "query": ["Sydney"],
        "start": ["2026-01-01T00:00:00Z"],
        "end": ["2026-02-01T00:00:00Z"],
        "forecast_production": ["True"],
        "format": ["json"],
    }


def test_get_wind_power_site_sends_resource_id_as_query():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.get_wind_power_site(
            resource_id="wind-123",
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "GET"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_site"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["wind-123"],
        "format": ["json"],
    }


def test_create_wind_power_site_posts_required_and_supplied_optional_fields():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.create_wind_power_site(
            name="South Ridge",
            latitude=-33.8567,
            longitude=151.2152,
            capacity=5,
            rotor_diameter=120,
            allow_negative_power=False,
            grid_export_limit=0,
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "POST"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_site"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {
        "name": "South Ridge",
        "latitude": -33.8567,
        "longitude": 151.2152,
        "capacity": 5,
        "rotor_diameter": 120,
        "allow_negative_power": False,
        "grid_export_limit": 0,
    }


def test_patch_wind_power_site_preserves_explicit_false_and_zero_values():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.patch_wind_power_site(
            resource_id="wind-123",
            allow_negative_power=False,
            grid_export_limit=0,
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "PATCH"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_site"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {
        "resource_id": "wind-123",
        "allow_negative_power": False,
        "grid_export_limit": 0,
    }


def test_update_wind_power_site_puts_required_fields_as_json():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.update_wind_power_site(
            resource_id="wind-123",
            name="South Ridge",
            latitude=-33.8567,
            longitude=151.2152,
            capacity=5,
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "PUT"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_site"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {
        "resource_id": "wind-123",
        "name": "South Ridge",
        "latitude": -33.8567,
        "longitude": 151.2152,
        "capacity": 5,
    }


def test_delete_wind_power_site_sends_resource_id_as_query():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = wind_power_sites.delete_wind_power_site(
            resource_id="wind-123",
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "DELETE"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/resources/wind_power_site"
    assert parse_qs(parsed_url.query) == {"resource_id": ["wind-123"]}
