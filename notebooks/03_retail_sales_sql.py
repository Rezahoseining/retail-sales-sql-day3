import pandas as pd
import sqlite3
import os

# -----------------------------------------------------------
# 1. Load Data
# -----------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "raw_superstore.csv")

df = pd.read_csv(csv_path, encoding="latin1")
print("[INFO] Data Loaded Successfully!")
print(df.head(), "\n")

# -----------------------------------------------------------
# 2. Create SQLite DB and Write Data
# -----------------------------------------------------------

db_path = os.path.join(BASE_DIR, "..", "data", "superstore.db")
conn = sqlite3.connect(db_path)

df.to_sql("Orders", conn, if_exists="replace", index=False)
print("[INFO] Data Written to SQLite Successfully!")

# Optional: Check table structure
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(Orders);")
print("\n[INFO] SQLite Table Structure:")
for row in cursor.fetchall():
    print(row)

# -----------------------------------------------------------
# 3. SQL Queries
# -----------------------------------------------------------

# ------------------------------
# Query 1: Top 10 Customers
# ------------------------------
query1 = """
SELECT 
    [Customer ID] AS CustomerID,
    COUNT([Order ID]) AS TotalOrders,
    SUM(Sales) AS TotalSales
FROM Orders
GROUP BY [Customer ID]
ORDER BY TotalSales DESC
LIMIT 10;
"""

customer_summary = pd.read_sql(query1, conn)
print("\n[Top Customers]")
print(customer_summary)

# ------------------------------
# Query 2: Top 10 Products by Sales
# ------------------------------
query2 = """
SELECT 
    [Product Name] AS ProductName,
    SUM(Sales) AS TotalSales
FROM Orders
GROUP BY [Product Name]
ORDER BY TotalSales DESC
LIMIT 10;
"""

product_summary = pd.read_sql(query2, conn)
print("\n[Top Products]")
print(product_summary)

# ------------------------------
# Query 3: Profit by Category
# ------------------------------
query3 = """
SELECT 
    Category,
    SUM(Profit) AS TotalProfit
FROM Orders
GROUP BY Category
ORDER BY TotalProfit DESC;
"""

category_profit = pd.read_sql(query3, conn)
print("\n[Profit by Category]")
print(category_profit)

# -----------------------------------------------------------
# 4. Close Connection
# -----------------------------------------------------------
conn.close()
print("\n[INFO] SQLite Connection Closed Successfully!")
