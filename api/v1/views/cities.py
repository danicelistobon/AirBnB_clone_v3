#!/usr/bin/python3
"""Cities file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=['GET', 'POST'])
def cities(state_id):
    """methods GET and POST of the cities by states (state_ID)
    """
    cities_st = storage.get("State", state_id)

    if cities_st is None:
        abort(404)

    if request.method == 'GET':
        cities_list = []
        for city in cities_st.cities:
            cities_list.append(city.to_dict())
        return jsonify(cities_list)

    if request.method == 'POST':
        json_city = request.get_json()
        if json_city is None:
            abort(400, "Not a JSON")
        if not json_city.get("name"):
            abort(400, "Missing name")
        json_city["state_id"] = state_id
        city = City(**json_city)
        storage.new(city)
        storage.save()
        storage.reload()
        return jsonify(city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=['GET', 'DELETE', 'PUT'])
def cities_id(city_id):
    """methods GET, DELETE and PUT of the cities by city_ID
    """
    city = storage.get("City", city_id)

    if city is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_city = request.get_json()
        if json_city is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at', 'state_id']:
                setattr(city, key, value)
        storage.save()
        return jsonify(city.to_dict()), 200
