import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.analytics import (
    average_order_value,
    category_revenue,
    load_sales,
    monthly_revenue,
    top_customers,
    top_products,
    total_orders,
    total_revenue,
)
from app.recommender import ProductRecommender


st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="🛍️",
    layout="wide",
)

st.title("🛍️ E-Commerce Sales Analytics & Recommendations")
st.caption("Python • Pandas • SQL • Scikit-learn • Streamlit")

sales = load_sales()
products = pd.read_csv("data/products.csv")

st.sidebar.header("Filters")
categories = ["All"] + sorted(sales["category"].unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)

filtered = sales.copy()

if selected_category != "All":
    filtered = filtered[filtered["category"] == selected_category]

c1, c2, c3 = st.columns(3)
c1.metric("Total Revenue", f"₹{total_revenue(filtered):,.0f}")
c2.metric("Total Orders", total_orders(filtered))
c3.metric("Average Order Value", f"₹{average_order_value(filtered):,.0f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Revenue by Category")
    category_df = category_revenue(filtered)

    fig, ax = plt.subplots()
    ax.bar(category_df["category"], category_df["revenue"])
    ax.set_ylabel("Revenue (₹)")
    ax.tick_params(axis="x", rotation=30)
    st.pyplot(fig)

with right:
    st.subheader("Monthly Revenue")
    monthly_df = monthly_revenue(filtered)

    fig, ax = plt.subplots()
    ax.plot(monthly_df["month"], monthly_df["revenue"], marker="o")
    ax.set_ylabel("Revenue (₹)")
    ax.tick_params(axis="x", rotation=30)
    st.pyplot(fig)

st.subheader("Top Selling Products")
st.dataframe(top_products(filtered), use_container_width=True)

st.subheader("Top Customers")
st.dataframe(top_customers(filtered), use_container_width=True)

st.divider()

st.header("Product Recommendations")

recommender = ProductRecommender(products)

product_options = dict(
    zip(products["product_name"], products["product_id"])
)

selected_product = st.selectbox(
    "Select a product",
    list(product_options.keys()),
)

if st.button("Recommend Similar Products"):
    recommendations = recommender.recommend(
        product_options[selected_product],
        n=5,
    )

    if recommendations.empty:
        st.warning("Product not found.")
    else:
        st.dataframe(
            recommendations[
                [
                    "product_name",
                    "category",
                    "brand",
                    "price",
                    "similarity",
                ]
            ],
            use_container_width=True,
        )
