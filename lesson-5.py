import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#----------------------------------------------------------------
#1
dtype = reviews.points.dtype

#----------------------------------------------------------------
#2
point_strings = reviews.points.astype(str)

#----------------------------------------------------------------
#3
n_missing_prices = reviews.price.isnull().sum()

#----------------------------------------------------------------
#4
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)