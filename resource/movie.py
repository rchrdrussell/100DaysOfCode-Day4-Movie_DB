#This file will move all route related codes from app.py to movies.py
#Flask-Restful uses Class-based syntax, so if you want to define a resource (API),
#we can just define a class which extends flask-restful's Resource
from flask import Response, request
from database.models import Movie
from flask_restful import Resource

#We will create two different classes: MoviesApi and MovieApi
#MoviesApi will be used to represent the whole document
#MovieApi will be used to manage each individual document
#The reason why these are separated is for organized and clean code.
class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return{'id': str(id)}, 200

class MovieApi(Resource):
    def put(self, id):
        body = request.get_json()
        movie = Movie().objects().get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        movie = Movie.objects().get(id=id).delete()
        return '', 200

    def get(self, id):
        movie = Movie.objects().get(id=id).to_json()
        return Response(movie, mimetype="applicaton/json", status = 200)

#For the Class to work, we need to register the endpoints
#Create a new file routes.py inside resources directory 
