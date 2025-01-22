import pandas as pd
from pandas import DataFrame
import numpy as np

col = ['movie_id','movie_title','release_date','video_release_date','IMDb_URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film_Noir','Horror','Musical','Mystery','Romance','Sci_Fi','Thriller','War','Western']
item_dataset = pd.read_csv('u.item.txt', delimiter = "|", header=None, names=col)

rating_item_list = []
for line in open('u.data.txt'):
    (user_id, item_id, rating, timestamp) = line.split('\t')

    rating_item = {'user_id': user_id, 'item_id': item_id,
                   'rating': rating, 'timestamp': timestamp
                   }
    rating_item_list.append(rating_item)

rating_dataset = DataFrame(rating_item_list)
rating_dataset['rating'] = pd.to_numeric(rating_dataset['rating'])

rating_list = []
for movie in item_dataset.iterrows():
    ratings = rating_dataset[rating_dataset['item_id'] == str(movie[1]['movie_id'])]
    average_rating = round(np.sum(ratings.iloc[:, 2]) / len(ratings.index), 2)
    rating_count = len(ratings.index)

    rating_object = { 
        'movie_id' : movie[1]['movie_id'], 
        'movie_title': movie[1]['movie_title'],
        'average_rating': average_rating,
        'rating_count': rating_count,
        'weighted_rating' : average_rating * rating_count
    }
    rating_list.append(rating_object)

rating_dataset = DataFrame(rating_list)

rating_dataset = rating_dataset.sort_values('weighted_rating', ascending=False)
rating_dataset.to_csv('rating_sorted_dataset.csv')
print(rating_dataset.iloc[0:10,:])
print(rating_dataset.iloc[-10:])

