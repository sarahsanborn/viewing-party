# ------------- WAVE 1 --------------------
import json

def create_movie(title, genre, rating):
    movie_dict = {}
    # if title == True and genre == True and rating == True:
    if True: 
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None 
    if title == None or genre == None or rating == None:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    # user_data is a dictionary with a key "watched" and value of list of dictionaries users have watched
        # An empty list value in user_data["watched"] means user has no movies in watched list
    # movie is a dictionary with title, genre, and rating keys
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    # user_data is a dictionary with key "watchlist" with value of list of dictionaries
    # movie is a dicitonary
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    # user_data is a dictionary with "watchlist" and "watched" keys
    # title is a string and reps the title of a movie the user has watched
    for movie in range(len(user_data["watchlist"])):
        for key,value in user_data["watchlist"][movie].items():
            if value == title:
                user_data["watched"].append(movie)
                user_data["watchlist"].pop(movie)
    # if user_data["watchlist"][0]["title"] == title:
    #     user_data["watched"] = [user_data["watchlist"][0]]
    #     user_data["watchlist"] = []
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # user_data is a dictionary with a "watched" list of movie dictionaries
    sum = 0
    for movie in range(len(user_data["watched"])):
        for key,value in user_data["watched"][movie].items():
            if key == "rating":
                sum += value
    if sum > 0:
        average = sum / len(user_data["watched"])
    else:
        average = 0.0
    return average

def get_most_watched_genre(user_data):
    genre_list = []
    genre_count = {}

    if user_data["watched"] == []:
        return None

    for movie in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][movie]['genre'])
        
    for i in genre_list:
        if i not in genre_count:
            count = 0
            genre_count[i] = count
        else:
            genre_count[i] = count + 1
    
    max_genre = max(genre_count, key =genre_count.get)
    print(genre_count)
    return max_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    ''' 
        user_data is a dictionary with "watched" (list of movie dictionaries) 
        "friends" (with a list of movie dictionaries of what friends have watched)
        returns list of dictionaries of unique movies the user has watched
    '''
    user_set = user_watched_list(user_data)
    friends_set = friend_watched_list(user_data)
    unique_movies_set = user_set - friends_set
    unique_movies_list = list(unique_movies_set)

    result_unique_movies = []

    for unique_movie in unique_movies_list:
        for movie in user_data["watched"]:
            if unique_movie == movie["title"]:
                result_unique_movies.append(movie)
    
    return result_unique_movies
    
def user_watched_list(user_data):
    user_watch_list = []
    
    for movie in user_data["watched"]:
        for key,value in movie.items():
            if key == "title":
                user_watch_list.append(value)
    set_user_watched = set(user_watch_list)
    return set_user_watched
    
def friend_watched_list(user_data):
    friends_watch_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            for key,value in movie.items():
                if key == "title":
                    friends_watch_list.append(value)
    set_friends_watched = set(friends_watch_list)
    return set_friends_watched

def get_friends_unique_watched(user_data):
    user_set = user_watched_list(user_data)
    friends_set = friend_watched_list(user_data)
    unique_movies_set = friends_set - user_set
    unique_movies_list = list(unique_movies_set)

    result_unique_movies = []

    for unique_movie in unique_movies_list:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                for key,value in movie.items():
                    if key == "title" and movie not in result_unique_movies:
                        if value == unique_movie:
                            result_unique_movies.append(movie)
    return result_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # print(json.dumps(user_data, indent=2))
    # return list of recommended movies
    # user has not watched
    # at least one friend has watched
    # "host" of the movie is in user's subscriptions
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        for host in user_data["subscriptions"]:
            if movie["host"] == host:
                recommended_movies.append(movie)
    return recommended_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    Returns a list of recommended movies for user
    Movie in list if user has not watched it, at least one of the user's friends has watched the movie
    The genre of the movie is the same as the user's most frequent genre
    '''
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    user_most_watched_genre = get_most_watched_genre(user_data)

    for movie in friends_watched:
        if movie["genre"] == user_most_watched_genre:
            recommended_movies.append(movie)
    
    return recommended_movies

def get_rec_from_favorites(user_data):
    '''
    Input: user_data which has a field "favorites" which contains a list of movie dictionaries (user's favorite movies)
    Output: Returns a list of recommended movies
    '''
    recommended_movies = []
    user_unique_movies = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in user_unique_movies:
            recommended_movies.append(movie)
    # for every movie in favorites
    # if movie in user_unique_movies
    # append to recommended movies
    
    return recommended_movies