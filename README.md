# Retail Sales SQL - Day 3

**Project:** Retail Superstore Dataset Analysis  
**Day:** 3  
**Tools:** Python, pandas, SQLite  

## Overview
In this project, we practice **SQL queries** on the Retail Superstore dataset using Python and SQLite.  
Key goals:
- Load dataset into SQLite in-memory database
- Calculate KPIs using SQL
- Practice GROUP BY, SUM, COUNT, RANK, JOIN queries
- Extract top customers and top products

## Folder Structure
retail-sales-sql-day3/
├── data/
│ └── raw_superstore.csv
├── notebooks/
│ └── 03_retail_sales_sql.py
├── README.md


## How to Run
1. Ensure Python 3.x is installed.
2. Install dependencies:
    ```bash
    pip install pandas

3. Run the script:
    python notebooks/03_retail_sales_sql.py



# Retail Sales SQL Analysis - Day 3

**هدف پروژه:**  
تمرین SQL روی دیتاست Retail Superstore با استفاده از SQLite و Python.

**فایل‌ها:**
- `03_retail_sql_analysis.py` : فایل اصلی با کوئری‌های SQL
- `data/raw_superstore.csv` : دیتاست فروش
- `retail_superstore.db` : دیتابیس SQLite ساخته شده توسط اسکریپت

**مباحث آموزش داده شده:**
- بارگذاری داده با pandas
- ایجاد دیتابیس SQLite
- نوشتن کوئری‌های SQL:
  - GROUP BY
  - COUNT, SUM
  - RANK() OVER
  - JOIN
