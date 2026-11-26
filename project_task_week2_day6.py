
import pandas as pd
import numpy as np
from pathlib import Path
from great_expectations.dataset import PandasDataset
from datetime import datetime
import html

# --------------------------------------------------
# W2D6: DATA GOVERNANCE
# Dataset: Sample - Superstore.csv
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data_governance"
OUTPUT_DIR.mkdir(exist_ok=True)

DATASET_PATH = BASE_DIR / "Sample - Superstore.csv"

# 1. Load dataset
df = pd.read_csv(DATASET_PATH, encoding="cp1252")

print("Dataset loaded successfully")
print("Shape:", df.shape)

# --------------------------------------------------
# 2. DAMA DATA QUALITY SCORECARD
# --------------------------------------------------

quality_checks = {
    "Completeness": (
        df[["Order ID", "Customer ID", "Product ID"]]
        .isnull().sum().sum() == 0
    ),
    "Accuracy": (
        (df["Sales"] >= 0).all()
        and (df["Quantity"] >= 1).all()
        and df["Discount"].between(0, 1).all()
    ),
    "Consistency": (
        pd.to_datetime(df["Order Date"], errors="coerce")
        .le(pd.to_datetime(df["Ship Date"], errors="coerce"))
        .all()
    ),
    "Timeliness": None,  # No ingestion timestamp or SLA in source data
    "Uniqueness": df["Row ID"].is_unique,
    "Validity": df["Category"].isin(
        ["Furniture", "Office Supplies", "Technology"]
    ).all()
}

scorecard_rows = []

for dimension, passed in quality_checks.items():
    if passed is None:
        status = "Not measurable"
        score = "N/A"
    else:
        status = "Pass" if passed else "Needs improvement"
        score = 1 if passed else 0

    scorecard_rows.append({
        "Dimension": dimension,
        "Result": status,
        "Score": score
    })

scorecard = pd.DataFrame(scorecard_rows)
scorecard.to_csv(
    OUTPUT_DIR / "dama_quality_assessment.csv",
    index=False
)

# --------------------------------------------------
# 3. GREAT EXPECTATIONS: 8 EXPECTATIONS
# --------------------------------------------------

def create_validator(data):
    validator = PandasDataset(data.copy())

    validator.expect_column_values_to_be_unique("Row ID")
    validator.expect_column_values_to_not_be_null("Order ID")
    validator.expect_column_values_to_not_be_null("Customer ID")
    validator.expect_column_values_to_not_be_null("Product ID")
    validator.expect_column_values_to_be_between(
        "Sales", min_value=0
    )
    validator.expect_column_values_to_be_between(
        "Quantity", min_value=1
    )
    validator.expect_column_values_to_be_between(
        "Discount", min_value=0, max_value=1
    )
    validator.expect_column_values_to_be_in_set(
        "Category",
        ["Furniture", "Office Supplies", "Technology"]
    )

    return validator.validate()

# Validate original dataset
original_result = create_validator(df)

print("\nOriginal data validation:")
print("Success:", original_result["success"])

# --------------------------------------------------
# 4. INJECT THREE INTENTIONAL DATA ERRORS
# --------------------------------------------------

test_df = df.copy()

# Error 1: Missing customer ID
test_df.loc[test_df.index[0], "Customer ID"] = np.nan

# Error 2: Negative sales value
test_df.loc[test_df.index[1], "Sales"] = -999

# Error 3: Invalid discount value
test_df.loc[test_df.index[2], "Discount"] = 1.5

# Validate intentionally corrupted data
error_result = create_validator(test_df)

print("\nInjected-error validation:")
print("Success:", error_result["success"])

# --------------------------------------------------
# 5. CREATE HTML VALIDATION REPORT
# --------------------------------------------------

def result_table(result, heading):
    rows = ""

    for item in result["results"]:
        expectation = item["expectation_config"][
            "expectation_type"
        ]
        status = "PASS" if item["success"] else "FAIL"

        rows += f"""
        <tr>
            <td>{html.escape(expectation)}</td>
            <td>{status}</td>
        </tr>
        """

    overall = "PASS" if result["success"] else "FAIL"

    return f"""
    <h2>{heading}</h2>
    <p><strong>Overall result:</strong> {overall}</p>
    <table border="1" cellpadding="8">
        <tr><th>Expectation</th><th>Result</th></tr>
        {rows}
    </table>
    """

report_html = f"""
<html>
<head>
<title>Great Expectations Validation Report</title>
<style>
body {{ font-family: Arial; margin: 30px; }}
table {{ border-collapse: collapse; }}
th {{ background: #eeeeee; }}
td, th {{ padding: 8px; }}
</style>
</head>
<body>
<h1>Week 2 Day 6 - Data Quality Validation</h1>
<p>Dataset: Sample - Superstore.csv</p>
<p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>

{result_table(original_result, "Original Dataset")}
{result_table(error_result, "Dataset with Injected Errors")}

</body>
</html>
"""

(OUTPUT_DIR / "great_expectations_report.html").write_text(
    report_html,
    encoding="utf-8"
)

# --------------------------------------------------
# 6. CREATE DATA QUALITY SCORECARD
# --------------------------------------------------
# 7. CREATE DATA QUALITY SCORECARD
# --------------------------------------------------

recommendations = """
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
"""

(OUTPUT_DIR / "data_quality_scorecard.md").write_text(
    recommendations,
    encoding="utf-8"
)

print("\nAll W2D6 files generated in:", OUTPUT_DIR)
print("Great Expectations report generated.")
print("DAMA scorecard generated.")
