import requests

class MovieModel:
    def __init__(self,title, rating, small_cover_image, summary):
        self.title = title
        self.rating = rating
        self.small_cover_image = small_cover_image
        self.summary = summary

def callMovieApi():
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=5
    '''
    response = requests.get(url)

    responseDict = response.json()
    movieapi = responseDict["data"]["movies"]

    return movieapi
    
        

def convert_model(movieapi):
    list = {}
    for movie in movieapi:
        movie_model = MovieModel(
            movie["title"],
            movie["rating"],
            movie["small_cover_image"],
            movie["summary"]
        )
        list.update(movie_model.__dict__)

    print(list)
    return list
