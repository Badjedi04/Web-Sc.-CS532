import pandas as pd
import numpy as np

# Load movie data
movie_data = pd.read_csv('basic.csv', delimiter="\t")

# Load rating data
rating_data = pd.read_csv('ratings.csv', delimiter="\t")

# Load item dataset
col = ['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Childrens',
       'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci_Fi', 'Thriller', 'War', 'Western']
item_data = pd.read_csv('u.item.txt', delimiter="|", header=None, names=col)

# Filter movies based on titles in item dataset
filtered_movies = movie_data[movie_data['originalTitle'].isin(item_data['movie_title'])]

# Create a list of rating information for filtered movies
ratings_list = []
for movie in filtered_movies.itertuples():
    filtered_rating = rating_data[rating_data['tconst'] == movie.tconst]
    if len(filtered_rating.index) > 0:
        avg_rating = filtered_rating.iloc[0,1]
        num_votes = filtered_rating.iloc[0,2]
        rating_item = { 
            'tconst': movie.tconst, 
            'movie_title': movie.originalTitle,
            'avg_rating': avg_rating,
            'num_votes': num_votes,
            'weighted_rating':  avg_rating * num_votes
        }
        ratings_list.append(rating_item)

# Create a dataframe from the ratings list and sort it by weighted rating
final_rating_dataset = pd.DataFrame(ratings_list)
final_rating_dataset = final_rating_dataset.sort_values('weighted_rating', ascending=False)

# Print the top 10 and bottom 10 movies based on weighted rating
print(final_rating_dataset.head(10))
print(final_rating_dataset.tail(10))
