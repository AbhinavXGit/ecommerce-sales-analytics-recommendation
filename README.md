# E-Commerce Sales Analytics & Product Recommendation Platform

A beginner-friendly data/ML project using **Python, Pandas, SQL, Scikit-learn and Streamlit**.

## What it does

### Sales Analytics
- Total revenue
- Total orders
- Average order value
- Monthly revenue
- Category-wise revenue
- Top-selling products
- Top customers

### Product Recommendation
A simple **content-based recommendation system** uses product category, brand and description.

```text
Product Data
    ↓
Text Features
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Similar Product Recommendations
```

## Tech Stack

- Python
- Pandas
- SQLite / SQL
- Scikit-learn
- Streamlit
- Matplotlib

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app/streamlit_app.py
```

## Recommendation logic

The recommender combines:

```text
category + brand + description
```

TF-IDF converts this text into numerical vectors.

Cosine similarity measures how similar two products are.

For example, selecting a running shoe returns other products with similar footwear/sports descriptions.

## SQL analysis

`sql/analysis_queries.sql` contains queries for:

- Total revenue
- Total orders
- Average order value
- Revenue by category
- Top-selling products
- Top customers

## Interview explanation

> I built an e-commerce analytics and recommendation project using Python, Pandas, SQL and Scikit-learn. I cleaned sales data, calculated metrics such as revenue and average order value, and built a Streamlit dashboard. I also implemented a simple content-based recommendation system using TF-IDF and cosine similarity. I chose content-based filtering because it is easy to understand and does not require a large user-rating dataset.

## Future improvements

- Collaborative filtering
- User login
- Real-time database
- Deployment
- More recommendation features
