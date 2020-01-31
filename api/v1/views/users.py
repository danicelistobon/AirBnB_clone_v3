#!/usr/bin/python3
"""Users file
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET', 'POST'])
def users():
    """methods GET and POST of the users
    """
    if request.method == 'GET':
        users_list = []
        for user in storage.all("User").values():
            users_list.append(user.to_dict())
        return jsonify(users_list)

    if request.method == 'POST':
        json_user = request.get_json()
        if json_user is None:
            abort(400, "Not a JSON")
        if not json_user.get("email"):
            abort(400, "Missing email")
        if not json_user.get("password"):
            abort(400, "Missing password")
        user = User(**json_user)
        storage.new(user)
        storage.save()
        storage.reload()
        return jsonify(user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=['GET', 'DELETE', 'PUT'])
def users_id(user_id):
    """methods GET, DELETE and PUT of the users by user_ID
    """
    user = storage.get("User", user_id)

    if user is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(user.to_dict())

    if request.method == 'DELETE':
        storage.delete(user)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_user = request.get_json()
        if json_user is None:
            abort(400, "Not a JSON")
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at', 'email']:
                setattr(user, key, value)
        storage.save()
        return jsonify(user.to_dict()), 200
