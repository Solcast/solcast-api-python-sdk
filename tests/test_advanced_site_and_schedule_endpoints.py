import json
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from solcast import pv_power_sites, schedules, tmy
from solcast.api import Client, Response


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


def test_client_put_serializes_json_body_as_application_json():
    body = {"resource_id": "pv-resource", "name": "PV site"}
    client = Client(
        base_url="https://api.solcast.com.au",
        endpoint="resources/pv_power_site",
        response_type=Response,
    )

    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = client.put({"api_key": "test-key"}, json_body=body)

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "PUT"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == body


def test_tmy_advanced_pv_power_sends_resource_id_and_query_options():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = tmy.advanced_pv_power(
            resource_id="pv-resource",
            base_url="https://custom.example",
            hours=12,
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "GET"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/data/tmy/advanced_pv_power"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["pv-resource"],
        "hours": ["12"],
        "format": ["json"],
    }


def test_create_utility_scale_measurements_posts_json_to_resource_path():
    measurements = [{"period_end": "2026-01-01T00:30:00Z", "total_power": 1.25}]
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = pv_power_sites.create_utility_scale_site_measurements(
            resource_id="pv-resource",
            measurements=measurements,
            base_url="https://custom.example",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "POST"
    assert parsed_url.netloc == "custom.example"
    assert parsed_url.path == "/utility_scale_sites/pv-resource/measurements"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {"measurements": measurements}


def test_create_utility_scale_measurements_posts_single_record_as_one_item_array():
    measurement = {"period_end": "2026-01-01T00:30:00Z", "total_power": 1.25}
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = pv_power_sites.create_utility_scale_site_measurements(
            resource_id="pv-resource",
            measurements=[measurement],
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert parsed_url.path == "/utility_scale_sites/pv-resource/measurements"
    assert json.loads(request.data) == {"measurements": [measurement]}


def test_get_resource_schedule_sends_required_window_and_optional_issue_time():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = schedules.get_resource_schedule(
            resource_id="pv-resource",
            period_start="2026-01-01T00:00:00Z",
            period_end="2026-01-02T00:00:00Z",
            issue_time="2026-01-03T00:00:00Z",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "GET"
    assert parsed_url.path == "/manage/schedules"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["pv-resource"],
        "period_start": ["2026-01-01T00:00:00Z"],
        "period_end": ["2026-01-02T00:00:00Z"],
        "issue_time": ["2026-01-03T00:00:00Z"],
        "format": ["json"],
    }


def test_patch_resource_schedule_sends_schedule_changes_as_json():
    availability = [
        {
            "period_start": "2026-01-01T00:00:00Z",
            "period_end": "2026-01-01T01:00:00Z",
            "availability": 75,
        }
    ]
    curtailment = [
        {
            "period_start": "2026-01-01T01:00:00Z",
            "period_end": "2026-01-01T02:00:00Z",
            "curtailment": 0.5,
        }
    ]
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = schedules.patch_resource_schedule(
            resource_id="pv-resource",
            availability_schedule=availability,
            curtailment_schedule=curtailment,
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "PATCH"
    assert parsed_url.path == "/manage/schedules"
    assert parse_qs(parsed_url.query) == {}
    assert request.headers["Content-type"] == "application/json"
    assert json.loads(request.data) == {
        "resource_id": "pv-resource",
        "availability_schedule": availability,
        "curtailment_schedule": curtailment,
    }


def test_delete_resource_schedule_sends_schedule_type_without_format():
    with patch("solcast.api.urlopen", return_value=FakeResponse()) as mock_urlopen:
        response = schedules.delete_resource_schedule(
            resource_id="pv-resource",
            period_start="2026-01-01T00:00:00Z",
            period_end="2026-01-02T00:00:00Z",
            schedule_type="availability,curtailment",
            api_key="test-key",
        )

    request, parsed_url = capture_request(mock_urlopen)
    assert response.success is True
    assert request.method == "DELETE"
    assert parsed_url.path == "/manage/schedules"
    assert parse_qs(parsed_url.query) == {
        "resource_id": ["pv-resource"],
        "period_start": ["2026-01-01T00:00:00Z"],
        "period_end": ["2026-01-02T00:00:00Z"],
        "schedule_type": ["availability,curtailment"],
    }
