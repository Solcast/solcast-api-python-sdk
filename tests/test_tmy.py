from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from solcast import tmy
from solcast.unmetered_locations import load_test_locations_coordinates


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


def test_radiation_and_weather():
    lats, longs = load_test_locations_coordinates()

    res = tmy.radiation_and_weather(
        latitude=lats[0], longitude=longs[0], output_parameters=["dni", "ghi"]
    )

    assert res.success is True
    assert (res.to_pandas().columns == ["dni", "ghi"]).all()


def test_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()

    res = tmy.rooftop_pv_power(latitude=lats[0], longitude=longs[0], capacity=3)
    assert res.success is True


def test_fail_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()

    res = tmy.rooftop_pv_power(
        latitude=lats[0], longitude=longs[0], array_type="wrong", capacity=3
    )

    assert res.success is False
    assert res.code == 400
    assert res.exception == "The specified condition was not met for 'array_type'."


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
