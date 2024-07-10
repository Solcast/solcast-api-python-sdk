from typing import Optional

from .api import Client, PandafiableResponse
from .urls import (
    base_url,
    forecast_grid_aggregations,
    live_grid_aggregations,
)


def live(
    collection_id: str, aggregation_id: Optional[str], **kwargs
) -> PandafiableResponse:
    """
    Get live aggregation data for up to 7 days of data at a time for a requested collection or aggregation.

    Args:
        collection_id: a unique identifier for your collection.
        aggregation_id: a unique identifier that belongs to the requested collection.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=live_grid_aggregations,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "collection_id": collection_id,
            "aggregation_id": aggregation_id,
            "format": "json",
            **kwargs,
        }
    )


def forecast(
    collection_id: str, aggregation_id: Optional[str], **kwargs
) -> PandafiableResponse:
    """
    Get forecast aggregation data for up to 7 days of data at a time for a requested collection or aggregation.

    Args:
        collection_id: a unique identifier for your collection.
        aggregation_id: a unique identifier that belongs to the requested collection.
        **kwargs: additional keyword arguments to be passed through as URL parameters to the Solcast API

    See https://docs.solcast.com.au/ for full list of parameters.
    """
    client = Client(
        base_url=base_url,
        endpoint=forecast_grid_aggregations,
        response_type=PandafiableResponse,
    )

    return client.get(
        {
            "collection_id": collection_id,
            "aggregation_id": aggregation_id,
            "format": "json",
            **kwargs,
        }
    )
