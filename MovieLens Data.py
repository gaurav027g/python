import pandas as pd
col1 = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep = "\t", names = col1)
print(ratings.head())

col2 = ['movie_id', 'title' 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('u.item', sep = "|", names = col2)
print(movies.head())

movie_ratings = pd.merge(movies, ratings)
print(movie_ratings.head())