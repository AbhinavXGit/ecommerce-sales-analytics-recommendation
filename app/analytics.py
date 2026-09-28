import pandas as pd


def load_sales(path="data/sales.csv"):
    return pd.read_csv(path, parse_dates=["order_date"])


def total_revenue(df):
    return float(df["revenue"].sum())


def total_orders(df):
    return int(df["order_id"].nunique())


def average_order_value(df):
    orders = total_orders(df)
    return total_revenue(df) / orders if orders else 0.0


def category_revenue(df):
    return (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )


def top_products(df, n=10):
    return (
        df.groupby("product_name", as_index=False)["quantity"]
        .sum()
        .sort_values("quantity", ascending=False)
        .head(n)
    )


def monthly_revenue(df):
    return (
        df.assign(month=df["order_date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)["revenue"]
        .sum()
    )


def top_customers(df, n=10):
    return (
        df.groupby("customer_name", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(n)
    )
