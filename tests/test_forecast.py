from solcast import forecast
from solcast.unmetered_locations import (
    load_test_locations_coordinates,
    UNMETERED_LOCATIONS,
)


def test_radiation_and_weather():
    lats, longs = load_test_locations_coordinates()
    res = forecast.radiation_and_weather(
        latitude=lats[3], longitude=longs[3], output_parameters=["albedo"], hours=3
    )

    assert res.success is True
    assert (res.to_pandas().columns == ["albedo"]).all()
    assert res.to_dict()["forecasts"][0]["period"] == "PT30M"


def test_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()
    res = forecast.rooftop_pv_power(
        latitude=lats[3],
        longitude=longs[3],
        output_parameters=["pv_power_rooftop10"],
        hours=3,
        capacity=1,
    )

    assert res.success is True
    assert (res.to_pandas().columns == ["pv_power_rooftop10"]).all()
    assert res.to_dict()["forecasts"][0]["period"] == "PT30M"


def test_advanced_pv_power():
    res = forecast.advanced_pv_power(
        resource_id=UNMETERED_LOCATIONS["Sydney Opera House"]["resource_id"],
        hours=3,
        capacity=1,
    )
    assert res.success is True
