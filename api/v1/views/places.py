#!/usr/bin/python3
"""Cities file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City
from models.place import Place


@app_views.route("/cities/<city_id>/places", methods=['GET', 'POST'])
def places(city_id):
    """methods GET and POST of the cities by states (state_ID)
    """
    cities_st = storage.get("City", city_id)

    if cities_st is None:
        abort(404)

    if request.method == 'GET':
        places_list = []
        for place in storage.all("place").values():
            places_list.append(place.to_dict())
        return jsonify(places_list)

    if request.method == 'POST':
        json_place = request.get_json()
        if json_place is None:
            abort(400, "Not a JSON")
        if not json_place.get("name"):
            abort(400, "Missing name")
        if not json_place.get('user_id'):
            abort(400, "Missing user_id")

        user_json = storage.get("User", json_place.get("user_id"))
        if user_json is None:
            abort(404)
        json_place['city_id'] = city_id
        json_place['user_id'] = json_place.get('user_id')
        new_city = Place(**json_data)
        storage.new(city)
        storage.save()
        storage.reload()
        return jsonify(new_city.to_dict()), 201


@app_views.route("places/<place_id>", methods=['GET', 'DELETE', 'PUT'])
def place_id(place_id):
    """methods GET, DELETE and PUT of the cities by city_ID
    """
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        storage.delete(place)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_place = request.get_json()
        if json_place is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at', 'state_id']:
                setattr(place, key, value)
        storage.save()
        return jsonify(place.to_dict()), 200
