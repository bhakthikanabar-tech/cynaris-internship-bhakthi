# Week 2 - Day 1: Data Visualisation
# Project: EDA on Indian Business Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="cp1252")

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

sns.set_theme(style="whitegrid", palette="deep")
# 1. Line Chart - Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png', dpi=300)
plt.show()


# 2. Bar Chart - Sales by Product Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_category.png', dpi=300)
plt.show()


# 3. Scatter Plot - Sales vs Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category', alpha=0.6)
plt.title('Relationship Between Sales and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('sales_vs_profit.png', dpi=300)
plt.show()


# 4. Histogram - Profit Distribution
plt.figure(figsize=(9, 5))
sns.histplot(data=df,x='Profit',bins=40,kde=True,color='teal')
plt.axvline(0, color='red', linestyle='--', label='Break-even Point')
plt.title('Distribution of Profit Across Transactions')
plt.xlabel('Profit')
plt.ylabel('Number of Transactions')
plt.legend()
plt.tight_layout()
plt.savefig('profit_distribution.png', dpi=300)
plt.show()


# 5. Box Plot - Profit by Product Category
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='Category', y='Profit')
plt.title('Profit Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('profit_by_category.png', dpi=300)
plt.show()