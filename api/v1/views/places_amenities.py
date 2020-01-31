#!/usr/bin/python3
"""reviews file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route("/places/<place_id>/amenities", methods=['GET'])
def amenities_(place_id):
    """methods GET of the amenities by places (place_ID)
    """
    amenities_pl = storage.get("Place", place_id)

    if amenities_pl is None:
        abort(404)

    amenities_list = []
    for amenitie in amenities_pl.amenities:
        amenities_list.append(amenitie.to_dict())
    return jsonify(amenities_list)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=['DELETE', 'POST'])
def amenities_id_(review_id):
    """methods DELETE and POST of the amenities by place_ID and amenity_ID
    """
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    amenity = storage.get("Amenity", amenity_id)

    if amenity is None:
        abort(404)

    if request.method == 'DELETE':
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
        storage.save()
        return jsonify({}), 200

    if request.method == 'POST':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
        storage.save()
        return jsonify(amenity.to_dict()), 201
