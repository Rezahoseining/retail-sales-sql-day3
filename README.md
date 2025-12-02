# Retail Sales Analysis - SQL Day 3

این پروژه ادامه EDA فروشگاه خرده‌فروشی است و بر روی تحلیل داده‌ها با SQL در پایتون تمرکز دارد.

## هدف پروژه
- کار با SQLite و Pandas
- اجرای کوئری‌های SQL روی داده‌های واقعی فروشگاه
- محاسبه KPIهای مشتری، محصول و دسته‌بندی
- آماده‌سازی پروژه برای رزومه و گیت

## فایل‌ها
    - `data/raw_superstore.csv`: داده‌های خام فروشگاه
    - `notebooks/03_retail_sales_sql.py`: کد اصلی تحلیل و SQL


retail-sales-sql-day3/
│
├─ data/
│   └─ raw_superstore.csv
│
├─ notebooks/
│   └─ 03_retail_sales_sql.py
│
└─ README.md


## ابزارها
- Python 3.12
- Pandas
- SQLite3
- Matplotlib و Seaborn (برای نمودارها)

## نحوه اجرا
1. مطمئن شوید که فایل CSV در مسیر `data/` قرار دارد.
2. اجرای فایل پایتون:
    bash
    python notebooks/03_retail_sales_sql.py
3. نتایج در ترمینال نمایش داده می‌شود و خروجی‌ها به صورت CSV یا نمودار ذخیره خواهند شد.

خروجی‌ها

خلاصه مشتریان (Total Orders و Total Sales)

محصولات پرفروش

KPIهای منطقه‌ای