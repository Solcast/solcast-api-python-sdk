from solcast import historic
from solcast.unmetered_locations import load_test_locations_coordinates
import pandas as pd


def test_radiation_and_weather():
    lats, longs = load_test_locations_coordinates()

    res = historic.radiation_and_weather(
        latitude=lats[0],
        longitude=longs[0],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
        install_date="2022-10-01",
        capacity=1,
        time_zone=-3,
    )

    assert res.success is True
    assert len(res.to_dict()["estimated_actuals"]) == 3 * 48 + 1
    assert res.to_pandas().shape[0] == 145
    assert isinstance(res.to_pandas(), pd.DataFrame)


def test_rooftop_pv_power():
    lats, longs = load_test_locations_coordinates()

    res = historic.radiation_and_weather(
        latitude=lats[0],
        longitude=longs[0],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
        capacity=10,
    )

    assert res.success is True
    assert len(res.to_dict()["estimated_actuals"]) == 3 * 48 + 1
    assert ~res.to_pandas().isna().any().all()


def test_fail_duration_and_end_date():
    lats, longs = load_test_locations_coordinates()

    res = historic.radiation_and_weather(
        latitude=lats[0],
        longitude=longs[0],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
        end_date="2022-10-25T18:45:00.00Z",
    )

    assert res.success is False
    assert res.code == 400
    assert res.exception == "Must specify exactly one of duration or end_date"
