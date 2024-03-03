#!/usr/bin/python3
""" web app"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/100-hbnb')
def display_hbnb():
    """pop down"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    cache_id = uuid.uuid4()
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close sess"""
    storage.close()


if __name__ == '__main__':
   """ comment"""
   app.run(host='0.0.0.0', port=5000)
