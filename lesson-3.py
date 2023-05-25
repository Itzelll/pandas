import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#----------------------------------------------------------------
#1
median_points = reviews.points.median()


#----------------------------------------------------------------
#2
countries = reviews.country.unique()


#----------------------------------------------------------------
#3
reviews_per_country = reviews.country.value_counts()


#----------------------------------------------------------------
#4
centered_price = reviews.price - reviews.price.mean()


#----------------------------------------------------------------
#5
bargain = (reviews.points/reviews.price).idxmax()
bargain_wine = reviews.loc[bargain, "title"]


#----------------------------------------------------------------
6
tropical= reviews.description.map(
    lambda desc:
        "tropical" in desc).sum()

fruity= reviews.description.map(
    lambda desc:
        "fruity" in desc).sum()

descriptor_counts = pd.Series([tropical, fruity], index=["tropical", "fruity"])


#----------------------------------------------------------------
#7
def stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1


star_ratings = reviews.apply(stars, axis="columns")