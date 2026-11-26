# Data Cleaning Report

## 1. Dataset Information

- Original records: 9994
- Original columns: 21
- Original missing values: 0
- Original duplicate records: 0

## 2. Cleaning Operations

- Forward fill was not applied because this is a transaction-level dataset, not a continuous time-series dataset. Carrying values between unrelated orders could introduce incorrect information.
- Sales: Detected 1167 outliers and capped values using IQR bounds.
- Quantity: Detected 170 outliers and capped values using IQR bounds.
- Discount: Detected 856 outliers and capped values using IQR bounds.
- Profit: Detected 1881 outliers and capped values using IQR bounds.
- Removed leading and trailing whitespace from text fields and standardised categorical labels using title case.

## 3. Outlier Analysis

| Column   |   Lower Bound |   Upper Bound |   Outliers Detected | Treatment               |
|:---------|--------------:|--------------:|--------------------:|:------------------------|
| Sales    |     -271.71   |      498.93   |                1167 | Capped using IQR bounds |
| Quantity |       -2.5    |        9.5    |                 170 | Capped using IQR bounds |
| Discount |       -0.3    |        0.5    |                 856 | Capped using IQR bounds |
| Profit   |      -39.7241 |       70.8169 |                1881 | Capped using IQR bounds |

## 4. Before and After Comparison

| Metric            |   Before Cleaning |   After Cleaning |
|:------------------|------------------:|-----------------:|
| Total Records     |              9994 |             9994 |
| Total Columns     |                21 |               21 |
| Missing Values    |                 0 |                0 |
| Duplicate Records |                 0 |                0 |

## 5. Final Dataset Information

- Final records: 9994
- Final columns: 21
- Remaining missing values: 0
- Remaining duplicate records: 0


## 6. Conclusion

The dataset was cleaned through duplicate removal, appropriate missing-value treatment, IQR-based outlier capping and text standardisation. Before-and-after quality metrics were recorded to document the changes.