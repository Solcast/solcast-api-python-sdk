from solcast import live
from solcast.unmetered_locations import (
    load_test_locations_coordinates,
    UNMETERED_LOCATIONS,
)


def test_radiation_and_weather():
    lats, longs = load_test_locations_coordinates()

    res = live.radiation_and_weather(
        latitude=lats[0], longitude=longs[0], output_parameters=["dni", "ghi"]
    )

    assert res.success is True
    assert res.exception is None
    assert (res.to_pandas().columns == ["dni", "ghi"]).all()


def test_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()

    res = live.rooftop_pv_power(latitude=lats[0], longitude=longs[0], capacity=3)
    assert res.success is True


def test_fail_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()

    res = live.rooftop_pv_power(latitude=lats[0], longitude=longs[0])
    assert res.success is False
    assert res.code == 400
    assert res.exception == "'Capacity' must be greater than '0'."


def test_advanced_pv_power():
    res = live.advanced_pv_power(
        resource_id=UNMETERED_LOCATIONS["Sydney Opera House"]["resource_id"]
    )

    assert res.success is True
