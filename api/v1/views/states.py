#!/usr/bin/python3
"""States file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route("/states", methods=['GET', 'POST'])
def states():
    """Retrieves the list of all State objects: GET /api/v1/states
    """
    if request.methods == 'GET':
        states = []
        for state in storage.all("State").values():
            states.append(state.to_dict())
        return jsonify(states)
    if request.methods == 'POST':
        json = request.get_json()
        if json is None:
            abort(400, "Not a JSON")
        if json.get('name') is None:
            abort(400, "Missing name")
    return jsonify()


@app_views.route("/states/<state_id>", methods=['GET', 'DELETE'])
def states_id(state_id):
    """Retrieves a State object: GET /api/v1/states/<state_id>
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if request.method == "GET":
        return jsonify(state.to_dict())
    if request.method == "DELETE":
        storage.delete(state)
        storage.save()
        return jsonify({}), 200