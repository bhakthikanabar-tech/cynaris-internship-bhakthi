
# Data Quality Scorecard
## Dataset: Sample - Superstore.csv

| DAMA Dimension | Assessment | Recommendation |
|---|---|---|
| Completeness | Checked required order, customer and product IDs | Monitor missing identifiers |
| Accuracy | Checked sales, quantity and discount ranges | Investigate invalid numeric values |
| Consistency | Compared order date and ship date | Reject shipping dates before order dates |
| Timeliness | Cannot be measured without ingestion timestamps | Define a data freshness SLA |
| Uniqueness | Checked Row ID uniqueness | Monitor duplicate row IDs |
| Validity | Checked allowed product categories | Enforce approved category values |

## Improvement Recommendations

1. Add automated validation before loading data into dashboards.
2. Track missing values in required fields.
3. Reject negative sales and invalid discount values.
4. Monitor duplicate transaction identifiers.
5. Record ingestion timestamps to measure freshness.
6. Maintain a documented data contract.

Note: Timeliness cannot be scored from this CSV because it does not
contain ingestion timestamps or a delivery SLA.
