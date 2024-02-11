from solcast import tmy
from solcast.unmetered_locations import load_test_locations_coordinates


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

    res = tmy.rooftop_pv_power(latitude=lats[0], longitude=longs[0], array_type="wrong")

    assert res.success is False
    assert res.code == 400
    assert res.exception == "The specified condition was not met for 'Array Type'."
