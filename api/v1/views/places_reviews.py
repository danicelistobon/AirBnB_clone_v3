#!/usr/bin/python3
"""reviews file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route("/places/<place_id>/reviews", methods=['GET', 'POST'])
def reviews(place_id):
    """methods GET and POST of the reviews by places (place_ID)
    """
    reviews_pl = storage.get("Place", place_id)

    if reviews_pl is None:
        abort(404)

    if request.method == 'GET':
        reviews_list = []
        for review in reviews_pl.reviews:
            reviews_list.append(review.to_dict())
        return jsonify(reviews_list)

    if request.method == 'POST':
        json_review = request.get_json()
        if json_review is None:
            abort(400, "Not a JSON")
        if not json_review.get("user_id"):
            abort(400, "Missing user_id")
        user_json = storage.get("User", json_review.get("user_id"))
        if user_json is None:
            abort(404)
        if not json_review.get("text"):
            abort(400, "Missing text")
        json_review["city_id"] = json_review.get("city_id")
        json_review["user_id"] = json_review.get("user_id")
        review = Place(**json_review)
        storage.new(review)
        storage.save()
        storage.reload()
        return jsonify(review.to_dict()), 201


@app_views.route("reviews/<review_id>", methods=['GET', 'DELETE', 'PUT'])
def reviews_id(review_id):
    """methods GET, DELETE and PUT of the places by place_ID
    """
    review = storage.get("Review", review_id)

    if review is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(review.to_dict())

    if request.method == 'DELETE':
        storage.delete(review)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_place = request.get_json()
        if json_place is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at', 'user_id',
                           'place_id']:
                setattr(review, key, value)
        storage.save()
        return jsonify(review.to_dict()), 200
