import os
import pandas as pd
import sqlite3

# -------------------------------
# 1. Load Data
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "raw_superstore.csv")

df = pd.read_csv(csv_path, encoding="latin1")  # utf-8 ممکن است خطا بدهد
print("[INFO] Data Loaded Successfully!")
print(df.head())

# -------------------------------
# 2. Create SQLite DB in memory
# -------------------------------
conn = sqlite3.connect(":memory:")  # دیتابیس موقت در حافظه
df.to_sql("Orders", conn, index=False, if_exists="replace")

# -------------------------------
# 3. SQL Queries
# -------------------------------

# 3.1 Total Orders and Sales per Customer
query1 = """
SELECT CustomerID, COUNT(OrderID) AS TotalOrders, SUM(Sales) AS TotalSales
FROM Orders
GROUP BY CustomerID
ORDER BY TotalSales DESC
LIMIT 10;
"""
customer_summary = pd.read_sql(query1, conn)
print("\n[INFO] Top 10 Customers by Sales:")
print(customer_summary)

# 3.2 Top Products by Sales with Ranking
query2 = """
SELECT 
    ProductID,
    SUM(Sales) AS TotalSales,
    RANK() OVER (ORDER BY SUM(Sales) DESC) AS SalesRank
FROM Orders
GROUP BY ProductID
ORDER BY SalesRank
LIMIT 10;
"""
top_products = pd.read_sql(query2, conn)
print("\n[INFO] Top 10 Products by Sales:")
print(top_products)

# 3.3 Join example: Orders + Customer Names
query3 = """
SELECT o.OrderID, c.CustomerName, o.Sales, o.Profit
FROM Orders o
JOIN Orders c ON o.CustomerID = c.CustomerID
LIMIT 10;
"""
# توضیح: در این مثال باید دیتای Customers جدا باشد، برای سادگی دوباره از Orders استفاده کردیم
join_example = pd.read_sql(query3, conn)
print("\n[INFO] Join Example (Orders + Customers):")
print(join_example)

# -------------------------------
# 4. Close Connection
# -------------------------------
conn.close()
