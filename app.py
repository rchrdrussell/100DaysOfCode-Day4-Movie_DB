from flask import Flask, request, Response #imports Flask, request, Response class
from database.db import initialize_db #imports initialize_db function from db file
from database.models import Movie #imports Movie class from models.py file
app = Flask(__name__)

#Setting the configuration of MongoDB database.
#The host is in the format of: <host-url>/<database-name>
app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/#100DaysOfCode-Day4-Movie_DB' #Our database name is Movie_DB
        }
initialize_db(app)

#get_movies() is a function that will return the JSON value of the
#Movie class that was imported from database.models
@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json() #Get all objects from Movie, convert to JSON
    return Response(movies, mimetype="application/json", status = 200)

#This will be a GET method for only ONE document from the server
@app.route('/movies/<id>')
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status = 200)

#POST a new movie in its JSON file to the Movie database
@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save() #** is called the spread operator. Spreads the dict
    #Movie(**body) becomes:
    #Movie(name = "Name of the movie", casts=["cast array"], genres=["genre array"])
    id = movie.id 
    return {'id': str(id)}, 200

#PUT (overwrite) an existing movie file to its respective id
@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.ge(id=id).update(**body)
    return '', 200

#DELETE an existing movie file from its respective id
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(index):
    Movie.objects.get(id=id).delete()
    return '', 200

#Flask server is started with app.run()
app.run()
