#!/usr/bin/python3
"""
web app
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    closeSession
    """
    storage.close()


@app.route('/101-hbnb/')
def hbnb_filters(the_id=None):
    """
    custom template
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('101-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users, cache_id=uuid.uuid4())

if __name__ == "__main__":
    """ comment"""
    app.run(host='0.0.0.0', port=5000)
