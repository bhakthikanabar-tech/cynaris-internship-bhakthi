# IndiaMART B2B Lead Scoring – Week 1 Report

## 1. Project Overview

The objective of this project is to develop a lead scoring model for a B2B marketplace sales team.
The proposed system will use historical lead information to predict lead quality and assign each lead a score between 0 and 100.
The goal is to help the sales team identify high-potential leads, prioritize follow-ups, and improve sales conversion efficiency.
The planned model will use Logistic Regression, with its performance evaluated using metrics such as AUC and false-positive rate.

## 2. Stakeholder Requirements

The sales team requires a lead scoring solution that:

1. Assigns every lead a quality score between 0 and 100.
2. Uses relevant lead attributes such as industry, company size, enquiry type, response time, and number of RFQs.
3. Helps sales representatives prioritize high-potential leads.
4. Uses Logistic Regression to predict lead quality.
5. Exports lead scores into a CRM-ready CSV file.
6. Provides an understandable explanation of the model and its important features.

### Expected Project Outcomes

- Achieve a test-set AUC of at least 0.72.
- Maintain a false-positive rate below 25% at a score threshold of 60.
- Generate scores for 5,000 new leads.
- Document feature importance and business insights in a Jupyter Notebook.

## 3. Analytical Questions

The following business questions will guide the initial analysis:

1. Which B2B product categories generate the highest order value and order volume?
2. Which payment terms are associated with higher order values and better delivery performance?
3. Do repeat buyers contribute more revenue than non-repeat buyers?
4. Which customer cities and acquisition channels generate the highest revenue?
5. Which product categories have the highest stock availability, monthly sales, and estimated profit margins?

## 4. Data Inventory

Three datasets were provided for the IndiaMART B2B project.

| Dataset                  | Rows | Columns | Missing Values | Duplicates |
| ------------------------ | ---: | ------: | -------------: | ---------: |
| da_b2b_orders.csv        |  600 |      13 |              0 |          0 |
| da_product_catalogue.csv |   50 |       7 |              0 |          0 |
| da_customer_profiles.csv |  200 |      10 |              0 |          0 |

### 4.1 B2B Orders Dataset

Contains order-related information, including:

- Order ID, buyer ID and seller ID
- Product category and order date
- Quantity, unit price and total order value
- Payment terms and delivery days
- On-time delivery, return quantity and repeat buyer status

### 4.2 Product Catalogue Dataset

Contains product-related information, including:

- Product ID and product name
- Category
- Maximum Retail Price (MRP)
- Cost of Goods Sold (COGS)
- Available stock units
- Average monthly sales

### 4.3 Customer Profiles Dataset

Contains customer-related information, including:

- Customer ID, city, age band and gender
- Acquisition channel
- First and last purchase dates
- Total orders and total revenue
- Customer churn status

## 5. Data Quality Assessment

The three datasets were inspected using Python and Pandas.

### 5.1 Completeness

- No missing values were identified in any of the three datasets.
- All inspected columns contained populated records.

### 5.2 Duplicate Records

- No duplicate rows were found in the B2B orders dataset.
- No duplicate rows were found in the product catalogue dataset.
- No duplicate rows were found in the customer profiles dataset.

### 5.3 Data Types

- Numerical fields include order quantities, prices, revenue, delivery days and stock units.
- Categorical fields include product categories, payment terms, cities and acquisition channels.
- Date fields are currently stored as text and may require conversion to datetime format during further analysis.

### 5.4 Dataset Relationship Assessment

The following checks were performed:

- No matching IDs were found between `buyer_id` in orders and `Customer_ID` in customer profiles.
- No matching categories were found between the orders and product catalogue datasets.
- The orders dataset does not contain a `Product_ID` column.
  Therefore, the datasets cannot currently be reliably joined using the available fields.

## 6. Data Limitations

During the initial data assessment, the following limitations were identified:

1. The project brief requires lead-related information such as industry, company size, enquiry type, response time and number of RFQs. These fields are not available in the three supplied datasets.
2. The datasets do not contain a common matching buyer/customer ID.
3. The orders and product catalogue datasets have different category values, preventing a direct category-based join.
4. The orders dataset does not contain a Product_ID field.
5. The supplied datasets do not contain a lead conversion or lead quality label required to train a supervised lead scoring model.

### Conclusion

The supplied datasets are suitable for preliminary B2B order, product and customer analysis. However, additional lead-level data and clarification from the stakeholder are required before developing the proposed lead scoring model.
