import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#----------------------------------------------------------------
#1
renamed = reviews.rename(columns={'region_1': 'region', "region_2": "locale"})

#----------------------------------------------------------------
#2
reindexed = reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

#----------------------------------------------------------------
#3
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products, movie_products])

#----------------------------------------------------------------
#4
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")


left = powerlifting_meets.set_index(['MeetID'])
right = powerlifting_competitors.set_index(['MeetID'])

powerlifting_combined = left.join(right)