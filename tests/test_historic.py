import pandas as pd

from solcast import historic
from solcast.unmetered_locations import (
    UNMETERED_LOCATIONS,
    load_test_locations_coordinates,
)


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


def test_advanced_pv_power():
    res = historic.advanced_pv_power(
        resource_id=UNMETERED_LOCATIONS["Sydney Opera House"]["resource_id"],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
    )

    assert res.success is True
    assert len(res.to_dict()["estimated_actuals"]) == 3 * 48 + 1
    assert ~res.to_pandas().isna().any().all()


def test_soiling_kimber():
    lats, longs = load_test_locations_coordinates()
    res = historic.soiling_kimber(
        latitude=lats[2],
        longitude=longs[2],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
        manual_washdates=["2022-10-01"],
    )
    assert res.success is True
    first = res.to_dict()["estimated_actuals"][0]
    assert first["period"] == "PT30M"
    df = res.to_pandas()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0


def test_soiling_hsu():
    lats, longs = load_test_locations_coordinates()
    res = historic.soiling_hsu(
        latitude=lats[3],
        longitude=longs[3],
        start="2022-10-25T14:45:00.00Z",
        duration="P3D",
    )
    assert res.success is True
    first = res.to_dict()["estimated_actuals"][0]
    assert first["period"] == "PT30M"
    df = res.to_pandas()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
