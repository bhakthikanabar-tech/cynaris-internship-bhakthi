# ==========================================
# WEEK 1 - DAY 4: SQL subqueries and Common Table Expressions (CTEs)
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

# Analysis 1: Above-Average Sales
above_avg_sales = pd.read_sql_query("""
    SELECT *
    FROM superstore
    WHERE Sales > (
        SELECT AVG(Sales)
        FROM superstore
    )
""", conn)
print("\n", "Total transactions above average sales:", len(above_avg_sales))
above_avg_sales.head()

# Analysis 2: Top-Performing Customer in Each Region
top_customers = pd.read_sql_query("""
    SELECT
        s1.Region,
        s1."Customer Name",
        SUM(s1.Sales) AS total_sales
    FROM superstore s1
    GROUP BY s1.Region, s1."Customer Name"
    HAVING SUM(s1.Sales) >= (
        SELECT SUM(s2.Sales)
        FROM superstore s2
        WHERE s2.Region = s1.Region
        GROUP BY s2."Customer Name"
        ORDER BY SUM(s2.Sales) DESC
        LIMIT 1
    )
""", conn)
print("\n", "Top-performing customers by region:")
print(top_customers)

# Analysis 3: Category-wise Sales Performance Using CTE
category_sales = pd.read_sql_query("""
    WITH CategorySales AS (
        SELECT
            Category,
            SUM(Sales) AS total_sales
        FROM superstore
        GROUP BY Category
    )
    SELECT *
    FROM CategorySales
    WHERE total_sales > (
        SELECT AVG(total_sales)
        FROM CategorySales
    )
    ORDER BY total_sales DESC
""", conn)
print("\nCategories with Above-Average Sales:")
print(category_sales)

# Analysis 4: Regional Sales Comparison Using Two CTEs
regional_sales = pd.read_sql_query("""
    WITH RegionSales AS (
        SELECT
            Region,
            SUM(Sales) AS total_sales
        FROM superstore
        GROUP BY Region
    ),
    AverageRegionSales AS (
        SELECT
            AVG(total_sales) AS avg_sales
        FROM RegionSales
    )
    SELECT
        Region,
        total_sales
    FROM RegionSales
    WHERE total_sales > (
        SELECT avg_sales
        FROM AverageRegionSales
    )
    ORDER BY total_sales DESC
""", conn)
print("\nRegions with Above-Average Sales:")
print(regional_sales)