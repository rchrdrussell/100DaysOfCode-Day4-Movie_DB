#Import Flask, request, and Response class from "flask" package
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/movie-bag'
        }
initialize_db(app)

#Using API tester to the path of `/movies` will output the list above
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="applicaton/json", status = 200)

#Create a POST request
@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return{'id': str(id)}, 200

#Create PUT request (update)
@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

#Create DELETE request
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200

#Create request to see only one movie
@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = Movie.objects.get(id=id).to_json()
    return Response(movie, mimetype="application/json", status=200)

app.run()
