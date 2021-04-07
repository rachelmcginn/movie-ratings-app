"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

# More code will go her
os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:    
    for movie in movie_data:
        title, overview, poster_path = (movie['title'],
                                        movie['overview'],
                                        movie['poster_path'])

        release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

        
    # TODO: create a movie here and append it to movies_in_db