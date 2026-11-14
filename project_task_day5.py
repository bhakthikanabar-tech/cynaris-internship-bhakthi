# ==========================================
# WEEK 1 - DAY 5: Python for data: Pandas Basic
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

# Create SQLite database connection
conn = sqlite3.connect(":memory:")

# Load Superstore dataset into SQLite
df.to_sql("superstore", conn, index=False, if_exists="replace")
print("Dataset loaded into SQLite successfully!")

# Task 2: Inspect the Dataset

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nDescriptive Statistics:")
print(df.describe())

# Value counts for categorical columns
print("\nCategory Value Counts:")
print(df['Category'].value_counts())

print("\nRegion Value Counts:")
print(df['Region'].value_counts())

# Select specific columns
selected_columns = df[['Order ID', 'Category', 'Sales', 'Profit']]
print("\nSelected Columns:")
print(selected_columns.head())

# Filter orders where Sales are greater than 500
high_sales = df[df['Sales'] > 500]
print("\nOrders with Sales greater than 500:")
print(high_sales.head())
print("Total high-sales orders:", len(high_sales))

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numerical values with column median
for column in df.select_dtypes(include=np.number).columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
for column in df.select_dtypes(include='object').columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Task 4: GroupBy and Aggregation

# Group sales and profit by category
category_analysis = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
})
print("\nCategory-wise Business Performance:")
print(category_analysis)

# Group sales by region
region_analysis = df.groupby('Region')['Sales'].sum()
print("\nRegion-wise Sales:")
print(region_analysis)

# Task 5: Export Cleaned Dataset to CSV
df.to_csv('cleaned_superstore.csv', index=False)
print("\nCleaned dataset exported successfully!")
print("File name: cleaned_superstore.csv")