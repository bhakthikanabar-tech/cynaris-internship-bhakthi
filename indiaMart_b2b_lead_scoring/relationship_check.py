    import pandas as pd
from pathlib import Path

folder = Path(__file__).parent

orders = pd.read_csv(folder / "da_b2b_orders.csv", encoding="cp1252")
products = pd.read_csv(folder / "da_product_catalogue.csv", encoding="cp1252")
customers = pd.read_csv(folder / "da_customer_profiles.csv", encoding="cp1252")

print("BUYER ID MATCH")
print("Matching IDs:", orders["buyer_id"].isin(customers["Customer_ID"]).sum())

print("\nPRODUCT CATEGORY MATCH")
print("Matching categories:", orders["category"].isin(products["Category"]).sum())

print("\nPRODUCT ID AVAILABLE IN ORDERS?")
print("Product_ID column:", "Product_ID" in orders.columns)

print("\nUNIQUE ORDER CATEGORIES:")
print(orders["category"].unique())

print("\nUNIQUE PRODUCT CATEGORIES:")
print(products["Category"].unique())