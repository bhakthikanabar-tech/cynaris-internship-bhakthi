# ==========================================
# WEEK 1 - DAY 2: SQL JOINS
# ==========================================
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import sqlite3
warnings.filterwarnings('ignore')

# Load your dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print("Dataset loaded successfully!")
print("\n--- DAY 2: SQL JOINS ---")

# Create Customers table
customers = df[
    ["Customer ID", "Customer Name", "Segment",
     "Country", "City", "State", "Region"]
].drop_duplicates(subset=["Customer ID"])

# Create Orders table
orders = df[
    ["Row ID", "Order ID", "Order Date", "Customer ID",
     "Product ID", "Category", "Sales", "Quantity", "Profit"]
].copy()

# Display table information
print("\nCustomers table:", customers.shape)
print("Orders table:", orders.shape)

print("\nCustomers preview:")
print(customers.head())

print("\nOrders preview:")
print(orders.head())

# Create SQLite database connection
conn = sqlite3.connect(":memory:")

# Store DataFrames as SQL tables
customers.to_sql("customers", conn, index=False, if_exists="replace")
orders.to_sql("orders", conn, index=False, if_exists="replace")

print("\nCustomers and Orders tables created successfully!")

# INNER JOIN: Orders with matching customer details
inner_join_query = """
SELECT
    o."Order ID",
    o."Customer ID",
    c."Customer Name",
    c."Segment",
    o."Category",
    o."Sales",
    o."Profit"
FROM orders o
INNER JOIN customers c
    ON o."Customer ID" = c."Customer ID";
"""

inner_join_result = pd.read_sql_query(inner_join_query, conn)

print("\n--- INNER JOIN RESULTS ---")
print(inner_join_result.head(10))

print("\nTotal joined records:", len(inner_join_result))

# Top 10 customers by total sales
top_customers_query = """
SELECT
    c."Customer ID",
    c."Customer Name",
    c."Segment",
    SUM(o."Sales") AS total_sales,
    SUM(o."Profit") AS total_profit
FROM orders o
INNER JOIN customers c
    ON o."Customer ID" = c."Customer ID"
GROUP BY
    c."Customer ID",
    c."Customer Name",
    c."Segment"
ORDER BY total_sales DESC
LIMIT 10;
"""

top_customers = pd.read_sql_query(top_customers_query, conn)

print("\n--- TOP 10 CUSTOMERS BY SALES ---")
print(top_customers)