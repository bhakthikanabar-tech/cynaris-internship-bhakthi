
# Week 2, Day 5 — NumPy for Data
# Project: EDA on Indian Business Dataset
# Actual dataset used: Sample - Superstore.csv

import os
import time
import numpy as np
import pandas as pd

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

df = pd.read_csv("Sample - Superstore.csv", encoding="cp1252")

print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

# Select numerical columns needed for analysis
numeric_df = df[["Sales", "Quantity", "Discount", "Profit"]].copy()

# Convert values to numeric and remove rows with missing values
numeric_df = numeric_df.apply(pd.to_numeric, errors="coerce")
numeric_df = numeric_df.dropna()

sales = numeric_df["Sales"].to_numpy()
quantity = numeric_df["Quantity"].to_numpy()
profit = numeric_df["Profit"].to_numpy()

# --------------------------------------------------
# 2. Create and manipulate NumPy arrays
# --------------------------------------------------

# 1D array
array_1d = np.array(sales[:6])

# 2D array
array_2d = np.array(numeric_df.iloc[:6].values)

# 3D array
array_3d = np.array(sales[:24]).reshape(2, 3, 4)

print("\n1D Array:")
print(array_1d)

print("\n2D Array:")
print(array_2d)

print("\n3D Array:")
print(array_3d)

# --------------------------------------------------
# 3. Vectorised operations
# --------------------------------------------------

print("\nVectorised Operations:")

print("Addition:", array_1d + 10)
print("Multiplication:", array_1d * 2)
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))

# Aggregate across axes
print("\n2D Array column totals (axis=0):")
print(np.sum(array_2d, axis=0))

print("\n2D Array row totals (axis=1):")
print(np.sum(array_2d, axis=1))

# --------------------------------------------------
# 4. NumPy broadcasting
# --------------------------------------------------

# Add a different adjustment to each column
column_adjustments = np.array([10, 2, 0.1, 5])

broadcast_result = array_2d + column_adjustments

print("\nBroadcasting Result:")
print(broadcast_result)

# --------------------------------------------------
# 5. Boolean masking and fancy indexing
# --------------------------------------------------

# Boolean masking: select sales greater than average sales
high_sales = sales[sales > np.mean(sales)]

print("\nNumber of transactions above average sales:")
print(len(high_sales))

print("First five high sales values:")
print(high_sales[:5])

# Fancy indexing: select specific positions
selected_sales = sales[[0, 1, 2, 3, 4]]

print("\nFancy Indexing Result:")
print(selected_sales)

# --------------------------------------------------
# 6. Statistical measures
# --------------------------------------------------

mean_sales = np.mean(sales)
std_sales = np.std(sales)
median_sales = np.median(sales)
percentile_25 = np.percentile(sales, 25)
percentile_75 = np.percentile(sales, 75)

sales_profit_correlation = np.corrcoef(sales, profit)[0, 1]

print("\nStatistical Analysis:")
print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Standard Deviation:", std_sales)
print("25th Percentile:", percentile_25)
print("75th Percentile:", percentile_75)
print("Sales-Profit Correlation:", sales_profit_correlation)

# --------------------------------------------------
# 7. Performance comparison on 1 million values
# --------------------------------------------------

# Create a 1-million-value array using the dataset's sales values
benchmark_data = np.resize(sales, 1_000_000)

# Python loop benchmark
start_time = time.perf_counter()

python_total = 0
for value in benchmark_data:
    python_total += value * 1.1

python_time = time.perf_counter() - start_time

# NumPy vectorised benchmark
start_time = time.perf_counter()

numpy_total = np.sum(benchmark_data * 1.1)

numpy_time = time.perf_counter() - start_time

print("\nPerformance Benchmark (1 million values):")
print("Python Loop Time:", python_time, "seconds")
print("NumPy Time:", numpy_time, "seconds")

if numpy_time > 0:
    print("Speed Improvement:", python_time / numpy_time, "times")

print("Python Result:", python_total)
print("NumPy Result:", numpy_total)

# --------------------------------------------------
# 8. Save analysis outputs
# --------------------------------------------------

output_folder = "numpy_analysis"
os.makedirs(output_folder, exist_ok=True)

# Save statistical results
statistics = pd.DataFrame({
    "Measure": [
        "Mean Sales",
        "Median Sales",
        "Standard Deviation",
        "25th Percentile",
        "75th Percentile",
        "Sales-Profit Correlation"
    ],
    "Value": [
        mean_sales,
        median_sales,
        std_sales,
        percentile_25,
        percentile_75,
        sales_profit_correlation
    ]
})

statistics.to_csv(
    os.path.join(output_folder, "numpy_statistics.csv"),
    index=False
)

# Save benchmark results
benchmark = pd.DataFrame({
    "Method": ["Python Loop", "NumPy Vectorisation"],
    "Execution Time (seconds)": [python_time, numpy_time],
    "Result": [python_total, numpy_total]
})

benchmark.to_csv(
    os.path.join(output_folder, "performance_benchmark.csv"),
    index=False
)

print("\nAnalysis completed successfully.")
print("Output files saved in:", output_folder)