#!/usr/bin/python3
"""Show states and cities by state views"""
from flask import Flask, render_template, g
import models
from models.state import State


app = Flask(__name__, template_folder='templates')


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_state_cities(id=None):
    """view that lists all cities by their states"""

    states = models.storage.all(State).values()
    if id:
        for state in states:
            if state.id == id:
                states = [state]
        if len(states) != 1:
            states = []
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def tear_down(error):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
