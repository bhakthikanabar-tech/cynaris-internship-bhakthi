import pandas as pd
from pathlib import Path

folder = Path(__file__).parent

files = [
    "da_b2b_orders.csv",
    "da_product_catalogue.csv",
    "da_customer_profiles.csv"
]

for file in files:
    print("\n" + "=" * 50)
    print("DATASET:", file)
    print("=" * 50)

    df = pd.read_csv(folder / file, encoding="cp1252")

    print("\nDataset Shape:", df.shape)
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())
    print("\nFirst 5 Rows:")
    print(df.head())