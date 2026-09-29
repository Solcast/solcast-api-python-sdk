from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Union, cast

if TYPE_CHECKING:
    import pandas as pd

MeasurementInput = Union[List[Dict[str, Any]], "pd.DataFrame"]
MAX_MEASUREMENTS_PER_REQUEST = 1000


def measurement_records(measurements: MeasurementInput) -> List[Dict[str, Any]]:
    if isinstance(measurements, list):
        records = measurements
    else:
        import pandas as pd

        if not isinstance(measurements, pd.DataFrame):
            raise TypeError("measurements must be a list or pandas DataFrame")

        frame = measurements
        if "period_end" not in frame.columns and frame.index.name == "period_end":
            frame = frame.reset_index()

        records = cast(List[Dict[str, Any]], frame.to_dict(orient="records"))
        for record in records:
            for field_name, value in record.items():
                if pd.api.types.is_scalar(value):
                    if pd.isna(value):
                        record[field_name] = None
                    elif hasattr(value, "isoformat"):
                        record[field_name] = value.isoformat()
                    elif hasattr(value, "item"):
                        record[field_name] = value.item()

    if len(records) > MAX_MEASUREMENTS_PER_REQUEST:
        raise ValueError(
            f"measurements cannot contain more than "
            f"{MAX_MEASUREMENTS_PER_REQUEST} records per request"
        )

    return records
