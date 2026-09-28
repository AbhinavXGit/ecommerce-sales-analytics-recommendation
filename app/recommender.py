import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ProductRecommender:
    def __init__(self, products: pd.DataFrame):
        self.products = products.copy()

        self.products["text"] = (
            self.products["category"].fillna("")
            + " "
            + self.products["brand"].fillna("")
            + " "
            + self.products["description"].fillna("")
        )

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.products["text"])
        self.similarity = cosine_similarity(self.matrix)

    def recommend(self, product_id, n=5):
        matches = self.products.index[
            self.products["product_id"] == product_id
        ].tolist()

        if not matches:
            return pd.DataFrame()

        index = matches[0]
        scores = list(enumerate(self.similarity[index]))
        scores.sort(key=lambda x: x[1], reverse=True)

        recommendations = []

        for idx, score in scores:
            if idx == index:
                continue

            row = self.products.iloc[idx].copy()
            row["similarity"] = round(float(score), 3)
            recommendations.append(row)

            if len(recommendations) == n:
                break

        return pd.DataFrame(recommendations)
