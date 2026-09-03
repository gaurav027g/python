import pandas as pd

col1 = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=col1)
print(ratings.head())

col2 = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('u.item', sep='|', names=col2)
print(movies.head())

movie_ratings = pd.merge(movies, ratings)
print(movie_ratings.head())

u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_csv('u.user', sep = '|', names = u_cols)
print(users.head())

lens = pd.merge(movie_ratings, users)
print(lens.head())

most_rated = lens.groupby('title').size().sort_values(ascending= False)[:20]
print(most_rated)

print(lens.title.value_counts()[:20])

import numpy as np
movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
print(movie_stats.head())

print(movie_stats.sort_values([('rating', 'mean')], ascending = False).head())


most_50 = lens.groupby('movie_id').size().sort_values(ascending = False)[:50]
print(most_50)