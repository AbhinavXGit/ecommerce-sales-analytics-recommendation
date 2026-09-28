import sqlite3
from pathlib import Path

import pandas as pd


DB_PATH = Path("ecommerce.db")


def create_database(sales_path="data/sales.csv"):
    sales = pd.read_csv(sales_path)

    conn = sqlite3.connect(DB_PATH)
    sales.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()


def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()
