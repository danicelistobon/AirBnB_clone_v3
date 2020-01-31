#!/usr/bin/python3

"""Amenity file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.amenity import Amenity


@app_views.route("/amenities", methods=['GET', 'POST'])
def amenities(state_id):
    """methods GET and POST of the cities by states (state_ID)
    """
    amenities_st = storage.get("State", state_id)

    if amenities_st is None:
        abort(404)

    if request.method == 'GET':
        amenities_list = []
        for amenity in amenities_st.amenities:
            amenities_list.append(amenity.to_dict())
        return jsonify(amenities_list)

    if request.method == 'POST':
        json_amenity = request.get_json()
        if json_amenity is None:
            abort(400, "Not a JSON")
        if not json_amenity.get("name"):
            abort(400, "Missing name")
        json_amenity["state_id"] = state_id
        amenity = Amenity(**json_amenity)
        storage.new(amenity)
        storage.save()
        storage.reload()
        return jsonify(amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", methods=['GET', 'DELETE', 'PUT'])
def amenities_id(amenity_id):
    """methods GET, DELETE and PUT of the cities by city_ID
    """
    amenity = storage.get("Amenity", amenity_id)

    if amenity is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(amenity.to_dict())

    if request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_amenity = request.get_json()
        if json_amenity is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at', 'state_id']:
                setattr(amenity, key, value)
        storage.save()
        return jsonify(amenity.to_dict()), 200
