import pandas as pd

df = pd.read_csv("../data/ratings_Electronics.csv")

top_products = df.groupby("productId")["rating"].mean()

recommendations = top_products.sort_values(ascending=False).head(10)

print(recommendations)
