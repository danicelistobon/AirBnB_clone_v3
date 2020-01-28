#!/usr/bin/python3
"""States file
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route("/states", methods=['GET'])
def states():
    """Retrieves the list of all State objects: GET /api/v1/states
    """
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route("/states/<state_id>", methods=['GET'])
def states_id(state_id):
    """Retrieves a State object: GET /api/v1/states/<state_id>
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())
