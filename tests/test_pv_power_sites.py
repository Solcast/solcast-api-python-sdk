import pytest

from solcast import pv_power_sites, unmetered_locations


def test_list_pv_power_sites():
    res = pv_power_sites.list_pv_power_sites()

    assert res.success
    assert isinstance(res.to_dict(), list)
    assert all(["resource_id" in resource for resource in res.to_dict()])
    with pytest.raises(
        AttributeError, match="'Response' object has no attribute 'to_pandas'"
    ):
        res.to_pandas()


def test_get_pv_power_sites():
    resource_id = unmetered_locations.UNMETERED_LOCATIONS["Sydney Opera House"][
        "resource_id"
    ]
    res = pv_power_sites.get_pv_power_site(resource_id=resource_id)
    assert res.success
    assert res.to_dict()["resource_id"] == resource_id
