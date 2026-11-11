# Week 1, Day 1 — SQL Fundamentals — SELECT, FROM, WHERE
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load your dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print("Dataset loaded successfully!")

# 2. Display first 10 records (SELECT * LIMIT 10)
print("\nFirst 10 Records:")
print(df.head(10))

# 3. Display dataset columns
print("\nDataset Columns:")
print(df.columns.tolist())

# 4. Select specific columns (SELECT)
selected_data = df[['Order ID', 'Customer Name',
                    'Category', 'Sales', 'Profit']]
print("\nSelected Columns:")
print(selected_data.head())

# 5. Filter records using a condition (WHERE)
high_sales = df[df['Sales'] > 500]
print("\nOrders with Sales Above 500:")
print(high_sales[['Order ID', 'Customer Name', 'Sales']].head(10))

# 6. Apply AND condition
high_sales_profit = df[
    (df['Sales'] > 500) & (df['Profit'] > 100)
]
print("\nOrders with Sales Above 500 AND Profit Above 100:")
print(high_sales_profit.head(10))

# 7. Apply OR condition
selected_categories = df[
    (df['Category'] == 'Furniture') |
    (df['Category'] == 'Technology')
]
print("\nFurniture OR Technology Orders:")
print(selected_categories.head(10))

# 8. Apply NOT condition
non_furniture = df[df['Category'] != 'Furniture']
print("\nOrders Excluding Furniture:")
print(non_furniture.head(10))

# 9. Apply BETWEEN condition
sales_range = df[df['Sales'].between(100, 1000)]
print("\nOrders with Sales Between 100 and 1000:")
print(sales_range.head(10))

# 10. Apply IN condition
selected_regions = df[df['Region'].isin(['East', 'West'])]
print("\nOrders from East and West Regions:")
print(selected_regions.head(10))

# 11. Apply LIKE equivalent using string matching
customer_filter = df[
    df['Customer Name'].str.startswith('A', na=False)
]
print("\nCustomers Whose Names Start With A:")
print(customer_filter[['Customer Name', 'Sales']].head(10))

# 12. Check missing values (IS NULL equivalent)
print("\nMissing Values:")
print(df.isnull().sum())

# 13. Basic dataset information
print("\nDataset Information:")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

# 14. Export filtered results
high_sales.to_csv('python_high_sales.csv', index=False)
print("\nFiltered results exported successfully!")