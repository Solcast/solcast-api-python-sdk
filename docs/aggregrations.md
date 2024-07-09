# Aggregations
More information in the [API Docs](https://docs.solcast.com.au/?#c1726d91-8a67-4803-89f4-02ecb5f03c05).

The module `aggregations` has 2 available methods:

| Endpoint            | API Docs                                                                                                |
|---------------------|---------------------------------------------------------------------------------------------------------|
| `live`              | [details](https://docs.solcast.com.au/#d1fc6dfa-a2f6-40db-a2b4-545030e33197){.md-button} |
| `forecast`          | [details](https://docs.solcast.com.au/#bda5d3ea-34fb-4f36-b0ca-d0a2d7c00629){.md-button}               |

### Example

```python
from solcast import aggregations

res = aggregations.forecast(
    collection_id="country_total",
    aggregation_id="it_total",
    output_parameters=['percentage', 'pv_estimate']
)

res.to_pandas().head()
```

| period_end                |   percentage |   pv_estimate |
|:--------------------------|-------------:|--------------:|
| 2024-06-13 04:30:00+00:00 |          1   |       333.499 |
| 2024-06-13 05:00:00+00:00 |          3.6 |      1157.39  |
| 2024-06-13 05:30:00+00:00 |          7   |      2268.41  |
| 2024-06-13 06:00:00+00:00 |         10.4 |      3361.17  |
| 2024-06-13 06:30:00+00:00 |         14.4 |      4630.91  |
