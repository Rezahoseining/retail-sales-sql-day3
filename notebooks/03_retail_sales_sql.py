import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# --- مسیر فایل CSV ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "raw_superstore.csv")

print(f"[INFO] Loading data from: {csv_path}")
df = pd.read_csv(csv_path, encoding="latin1")
print("[INFO] Data Loaded Successfully!")
print(df.head())

# --- اتصال به SQLite ---
db_path = os.path.join(BASE_DIR, "data", "retail_sales.db")

try:
    with sqlite3.connect(db_path) as conn:
        df.to_sql("Orders", conn, if_exists="replace", index=False)
        print("[INFO] Data Written to SQLite Successfully!")

        # --- بررسی ستون‌ها ---
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(Orders);")
        for col in cursor.fetchall():
            print(col)

        # --- Query 1: خلاصه مشتری ---
        query1 = """
        SELECT [Customer ID] AS CustomerID, COUNT([Order ID]) AS TotalOrders, SUM(Sales) AS TotalSales
        FROM Orders
        GROUP BY [Customer ID]
        ORDER BY TotalSales DESC
        LIMIT 10;
        """
        customer_summary = pd.read_sql(query1, conn)
        print("\n[INFO] Top 10 Customers:\n", customer_summary)

        # --- Query 2: محصولات پرفروش ---
        query2 = """
        SELECT [Product Name] AS ProductName, SUM(Sales) AS TotalSales
        FROM Orders
        GROUP BY [Product Name]
        ORDER BY TotalSales DESC
        LIMIT 10;
        """
        product_summary = pd.read_sql(query2, conn)
        print("\n[INFO] Top 10 Products:\n", product_summary)

        # --- Query 3: KPI منطقه‌ای ---
        query3 = """
        SELECT Region, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit
        FROM Orders
        GROUP BY Region;
        """
        region_kpi = pd.read_sql(query3, conn)
        print("\n[INFO] Region KPIs:\n", region_kpi)

except sqlite3.Error as e:
    print("[ERROR] SQLite error:", e)
