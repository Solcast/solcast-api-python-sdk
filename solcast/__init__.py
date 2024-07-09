__version__ = "1.2.6"

from . import (
    api,
    forecast,
    historic,
    live,
    tmy,
    aggregations,
    unmetered_locations,
    urls,
    pv_power_sites,
)

__all__ = [
    "aggregations",
    "forecast",
    "historic",
    "live",
    "tmy",
    "unmetered_locations",
    "pv_power_sites",
]
