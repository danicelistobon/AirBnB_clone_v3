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
    dir_number = { "amenities": storage.count("amenities"),
                   "cities": storage.count("cities"),
                   "places": storage.count("places"),
                   "reviews": storage.count("reviews"),
                   "states": storage.count("states"),
                   "users": storage.count("users")}
    return jsonify(dir_number)
