from flask import Blueprint, request, jsonify
from services.user_service import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route("/create", methods=["POST"])
def create_user():
    try:
        data = request.json
        user_id = UserService.create_user(data)
        return jsonify({"message": "User created", "id": user_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@users_bp.route("/all", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify(users)
