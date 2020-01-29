#!/usr/bin/python3
"""Index file
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """returns a JSON: "status": "OK"
    """
    dict_obj = {"status": "OK"}
    return jsonify(dict_obj)


@app_views.route('/stats')
def count():
    """endpoint that retrieves the number of each objects by type
    """
    dir_number = { "amenities": storage.count("Amenity"),
                   "cities": storage.count("City"),
                   "places": storage.count("Place"),
                   "reviews": storage.count("Review"),
                   "states": storage.count("State"),
                   "users": storage.count("User")}
    return jsonify(dir_number)
