from movie_model import MovieModel
import requests

def callMovieApi():
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=5
    '''
    response = requests.get(url)

    responseDict = response.json()
    movieapi = responseDict["data"]["movies"]

    return convert_model(movieapi)
    
        

def convert_model(movieapi):
    list = []
    for movie in movieapi:
        movie_model = MovieModel(
            movie["title"],
            movie["rating"],
            movie["small_cover_image"],
            movie["summary"]
        )
        list.append(movie_model)

    return list