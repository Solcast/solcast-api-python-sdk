import ast
import re
from pathlib import Path
from urllib.parse import urlsplit


SDK_ROOT = Path(__file__).resolve().parents[1]


def test_forecast_guide_lists_every_public_method_with_api_reference_links():
    forecast_tree = ast.parse(
        (SDK_ROOT / "solcast/forecast.py").read_text(encoding="utf-8")
    )
    public_methods = {
        node.name
        for node in forecast_tree.body
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
    }
    guide = (SDK_ROOT / "docs/forecast.md").read_text(encoding="utf-8")
    rows = re.findall(
        r"^\|\s*`([^`]+)`\s*\|\s*\[details\]\(([^)]+)\)",
        guide,
        re.MULTILINE,
    )
    documented_methods = {method for method, _href in rows}

    assert documented_methods == public_methods
    assert len(rows) == len(documented_methods)
    for method, href in rows:
        parsed_href = urlsplit(href)
        assert parsed_href.scheme == "https", method
        assert parsed_href.netloc == "docs.solcast.com.au", method
        assert parsed_href.fragment, method


def test_premium_forecast_guide_links_target_their_api_operations():
    guide = (SDK_ROOT / "docs/forecast.md").read_text(encoding="utf-8")
    rows = dict(
        re.findall(
            r"^\|\s*`([^`]+)`\s*\|\s*\[details\]\(([^)]+)\)",
            guide,
            re.MULTILINE,
        )
    )

    assert (
        urlsplit(rows["premium_pv_power"]).fragment == "getDataForecastPremiumPvPower"
    )
    assert (
        urlsplit(rows["premium_wind_power"]).fragment
        == "getDataForecastPremiumWindPower"
    )
