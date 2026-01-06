# 📊 Sales & Orders Data Analysis Project
## 📌 Project Overview
This project focuses on analyzing sales and order data to extract meaningful business insights using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**.  
The goal is to understand sales performance, profit trends, customer behavior, and payment preferences through data analysis and visualization.

---

## ❓ Problem Statement
Raw sales and order data is difficult to understand without proper analysis.  
Businesses need insights such as:
- Which product categories generate maximum sales and profit?
- Which payment modes are most preferred by customers?
- Which states and cities contribute the most to sales?
- Where are losses occurring?

This project solves these problems by transforming raw CSV data into clear visual insights.

---

## 📂 Dataset Description
The project uses **two CSV files**:

### 1️⃣ Details.csv
Contains sales-related information:
- `Order ID`
- `Amount`
- `Profit`
- `Quantity`
- `Category`
- `Sub-Category`
- `PaymentMode`

### 2️⃣ Orders.csv
Contains customer and order information:
- `Order ID`
- `Order Date`
- `CustomerName`
- `State`
- `City`

Both datasets are merged using **Order ID**.

---

## 🛠️ Technologies Used
- **Python**
- **Pandas** – data loading, cleaning, merging, and analysis
- **Matplotlib** – data visualization
- **Seaborn** – advanced and attractive statistical plots

---

## 🔄 Project Workflow
1. Loaded CSV datasets using Pandas  
2. Cleaned column names and checked for missing values  
3. Merged datasets using `Order ID`  
4. Performed Exploratory Data Analysis (EDA)  
5. Created multiple visualizations for better understanding  
6. Extracted business insights from the data  

---

## 📈 Visualizations Created
- Orders by Payment Mode (Bar Chart)
- Total Sales by Category
- Profit Distribution (Histogram)
- Sales Trend Over Time (Line Plot)
- Profit vs Sales (Scatter Plot)
- State vs Category Profit (Heatmap)
- Category & Sub-Category Sales Comparison
- Payment Mode Distribution (Pie / Donut Chart)

---

## 🔍 Key Insights
- Certain categories generate higher sales but lower profit.
- Some payment modes are more popular among customers.
- Sales performance varies significantly across states.
- Loss-making orders can be identified through profit analysis.

---

- Miss. Srushti Kandakur.