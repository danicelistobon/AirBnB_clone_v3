#!/usr/bin/python3
"""States file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route("/states", methods=['GET', 'POST'])
def states():
    """Retrieves the list of all State objects: GET /api/v1/states
    """
    if request.method == 'GET':
        states = []
        for state in storage.all("State").values():
            states.append(state.to_dict())
        return jsonify(states)
    if request.method == 'POST':
        json_state = request.get_json()
        if json_state is None:
            abort(400, "Not a JSON")
        if "name" not in json_state:
            abort(400, "Missing name")
        state = State()
        state.name = json_state['name']
        storage.new(state)
        storage.save()
        storage.reload()
        return jsonify(state.to_dict()), 200


@app_views.route("/states/<state_id>", methods=['GET', 'DELETE', 'PUT'])
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
    if request.method == "PUT":
        json_state = request.get_json
        if json_state is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        storage.save()
        return jsonify(state.to_dict()), 200
