# ==========================================
# WEEK 1 - DAY 3: SQL AGGREGATE FUNCTIONS
# ==========================================
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import sqlite3
warnings.filterwarnings('ignore')

# Load Dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='cp1252')
print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

# 1. Total Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("Total Sales by Region:")
print(region_sales)

# 2. Total Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\n","Total Sales by Category:")
print(category_sales)

# 3. Monthly Sales Analysis
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.month_name()
monthly_sales = df.groupby(['Month', 'Month Name'])['Sales'].sum().sort_index()
print("\nTotal Sales by Month:")
print(monthly_sales)

# 4. Categories with Total Sales Greater Than 100,000
high_sales_categories = category_sales[category_sales > 100000]
print("\n","Categories with Sales Above 100,000:")
print(high_sales_categories)

# 5. Cumulative Sales Analysis
df = df.sort_values('Order Date')
df['Cumulative Sales'] = df['Sales'].cumsum()
print("\n","Cumulative Sales:")
print(df[['Order Date', 'Sales', 'Cumulative Sales']].head(10))