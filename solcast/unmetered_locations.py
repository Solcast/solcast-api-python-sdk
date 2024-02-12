UNMETERED_LOCATIONS = {
    "Sydney Opera House": {
        "latitude": -33.856784,
        "longitude": 151.215297,
        "resource_id": "ba75-e17a-7374-95ed",
    },
    "Grand Canyon": {
        "latitude": 36.099763,
        "longitude": -112.112485,
        "resource_id": "375f-eb3e-71c0-ef5e",
    },
    "Stonehenge": {
        "latitude": 51.178882,
        "longitude": -1.826215,
        "resource_id": "1a57-6b1f-ec18-c5c8",
    },
    "The Colosseum": {
        "latitude": 41.89021,
        "longitude": 12.492231,
        "resource_id": "5f86-4c8f-2cb3-0215",
    },
    "Giza Pyramid Complex": {
        "latitude": 29.977296,
        "longitude": 31.132496,
        "resource_id": "8d10-f530-af85-5cbb",
    },
    "Taj Mahal": {
        "latitude": 27.175145,
        "longitude": 78.042142,
        "resource_id": "b926-8fd2-ad3f-e4f5",
    },
    "Fort Peck": {
        "latitude": 48.30783,
        "longitude": -105.1017,
        "resource_id": "3ae7-2456-492c-9aba",
    },
    "Goodwin Creek": {
        "latitude": 34.2547,
        "longitude": -89.8729,
        "resource_id": "b787-cf17-e429-ef1d",
    },
}


def load_test_locations_coordinates():
    """returns longitude, latitude and resource_id for the unmetered locations"""
    coords = [list(coords.values()) for coords in list(UNMETERED_LOCATIONS.values())]
    latitudes, longitudes = [c[0] for c in coords], [c[1] for c in coords]
    return latitudes, longitudes


def load_test_locations_names():
    """returns longitude, latitude and resource_id for the unmetered locations"""
    return list(UNMETERED_LOCATIONS.keys())
