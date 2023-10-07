#!/usr/bin/python3
""" Starts a Flask Web Application """
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove/closes the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """ Starting point of HBNB """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_lst = []

    for state in states:
        state_lst.append([state, sorted(state.cities, key=lambda k: k.name)])
        amenities = storage.all(Amenity).values()
        amenities = sorted(amenities, key=lambda k: k.name)
        places = storage.all(Place).values()
        places = sorted(places, key=lambda k: k.name)

        return render_template('0-hbnb.html',
                               states=state_lst,
                               amenities=amenities,
                               places=places,
                               cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Function entry point """
    app.run(host='0.0.0.0', port=5000)
