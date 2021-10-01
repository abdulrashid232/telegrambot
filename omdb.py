import os 
import requests

def movie_infor(movieTitle):
    api_key = os.getenv("Movie_api")
    url = "http://www.omdbapi.com/?apikey=" + api_key
    poster_url = "http://img.omdbapi.com/?apikey=" + api_key
    param = {"api_key":api_key, "t": movieTitle}
    response = requests.get(url, param).json()

    if response.get("Response") != "True":
        return None

    movie_info = {}
    movie_info["title"] = response.get("Title")
    movie_info["year"] = response.get("Year")
    movie_info["plot"] = response.get("Plot")
    movie_info["actors"] = response.get("Actors")
    movie_info["ratings"] = response.get("Ratings")
    movie_info["imdb_ratings"] = response.get("imdb_rating")
    movie_info['poster'] = response.get('Poster')


    return movie_info