import pandas as pd

def load_item_dataset():
    # Define column names for u.item file
    col = ['movie_id','movie_title','release_date','video_release_date','IMDb_URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film_Noir','Horror','Musical','Mystery','Romance','Sci_Fi','Thriller','War','Western']
    
    # Read u.item file into item_dataset DataFrame
    item_dataset = pd.read_csv('u.item.txt', delimiter='|', header=None, names=col)
    
    return item_dataset


def find_similar_users(age, gender, occupation):
    similar_user = []
    for line in open('u.user.txt'):
        (user_id, user_age, user_gender, user_occ, user_zip) = line.split('|')
        if user_age == age and user_gender == gender and user_occ == occupation:
            similar_user.append(user_id)
    
    return similar_user


def load_rating_dataset(item_dataset):
    # Create a list of dictionaries containing rating data for each item
    rating_item_list = []
    for line in open('u.data.txt'):
        (user_id, item_id, rating, timestamp) = line.split('\t')
        
        # Filter item_dataset to only include the current item
        item = item_dataset[item_dataset['movie_id'] == pd.to_numeric(item_id)]
        
        # Add current rating data to rating_item_list as a dictionary
        rating_item = {'user_id': user_id, 'item_id': item_id, 'item_name': item.iloc[0,1], 'rating': rating, 'timestamp': timestamp}
        rating_item_list.append(rating_item)
    
    # Convert rating_item_list to a DataFrame
    rating_dataset = pd.DataFrame(rating_item_list)
    
    return rating_dataset


def find_favorite_and_least_fav_films(similar_user, rating_dataset):
    favorite_films_list = []
    least_fav_films_list = []
    
    for user in similar_user[0:3]:
        user_rated_data = rating_dataset[rating_dataset['user_id'] == user]
        user_rated_data = user_rated_data.sort_values('rating', ascending=False)
        user_rated_data_fav_films = user_rated_data.iloc[0:3, :]
        user_rated_data_least_fav_films = user_rated_data.iloc[-3:]
        favorite_films_list.append(user_rated_data_fav_films)
        least_fav_films_list.append(user_rated_data_least_fav_films)
    
    return favorite_films_list, least_fav_films_list


if __name__ == '__main__':
    # Load item dataset
    item_dataset = load_item_dataset()
    
    # Find similar users
    similar_user = find_similar_users('30', 'M', 'student')
    
    # Load rating dataset
    rating_dataset = load_rating_dataset(item_dataset)
    
    # Find favorite and least favorite films for each user in similar_user
    favorite_films_list, least_fav_films_list = find_favorite_and_least_fav_films(similar_user, rating_dataset)
    
    # Print favorite and least favorite films for each user in similar_user
    for ds in favorite_films_list:
        print(ds.to_string(index=False))

    for lds in least_fav_films_list:
        print(lds.to_string(index=False))
