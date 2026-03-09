import pandas as pd

df = pd.read_csv("../data/ratings_Electronics.csv")

average_rating = df["rating"].mean()

print("Average Rating:", average_rating)
