import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#----------------------------------------------------------------
#1
desc = reviews.description


#----------------------------------------------------------------
#2
first_description = reviews.description[0]


#----------------------------------------------------------------
#3
first_row = reviews.iloc[0]


#----------------------------------------------------------------
#4
first_descriptions = reviews.description.iloc[:10]


#----------------------------------------------------------------
#5
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.iloc[indices]


#----------------------------------------------------------------
#6
indice = [0,1,10,100]
df = reviews.loc[indice, ['country', 'province', 'region_1', 'region_2']]


#----------------------------------------------------------------
#7
df = reviews.loc[0:99, ['country', 'variety']]


#----------------------------------------------------------------
#8
italian_wines = reviews.loc[reviews.country == 'Italy']


#----------------------------------------------------------------
#9
#opcion 1
top_oceania_wines = reviews.loc[(reviews.country == 'Australia' | reviews.country == 'Zealand') & (reviews.points >= 95)]

#opcion 2
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]