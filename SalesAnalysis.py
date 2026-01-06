import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

details = pd.read_csv("Details.csv")
orders = pd.read_csv("Orders.csv")

print(details.head())
print(orders.head())

# Merge both datasets on Order ID
df = pd.merge(details, orders, on="Order ID", #on: This is the common column in both files
               how="inner")  #INNER JOIN: “Keep only the orders that exist in both files”
print(df.head())
# Check size after merge
print("Rows, Columns:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values in each column:")
print(df.isnull().sum())

#Seaborn
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="PaymentMode")
plt.title("Number of Orders by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.show()

#Top 10 States by Sales
state_sales = df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(9,5))
state_sales.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.show()

#Category Vs Profit
plt.figure(figsize=(9,5))
sns.boxplot(data=df, x="Category", y="Profit")
plt.title("Profit by Category")
plt.xticks(rotation=30)
plt.show()

#Total sales by category
category_sales = df.groupby("Category")["Amount"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(
    data=category_sales,
    x="Category",
    y="Amount",
    palette="viridis"
)
plt.title("Total Sales by Category", fontsize=14)
plt.xticks(rotation=30)
plt.show()

#category vs Quantity
category_qty = df.groupby("Category")["Quantity"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(
    data=category_qty,
    x="Category",
    y="Quantity",
    palette="magma"
)
plt.title("Total Quantity Sold by Category", fontsize=14)
plt.xticks(rotation=30)
plt.show()

#Payment Mode Share
payment_counts = df["PaymentMode"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Payment Mode Distribution")
plt.show()

#Category & Sub-Category Sales
subcat_sales = df.groupby(["Category", "Sub-Category"])["Amount"].sum().reset_index()
plt.figure(figsize=(12,6))
sns.barplot(
    data=subcat_sales,
    x="Category",
    y="Amount",
    hue="Sub-Category",
    palette="tab10"
)
plt.title("Sales by Category & Sub-Category", fontsize=14)
plt.xticks(rotation=30)
plt.show()
