from flask import current_app
from models.user import User

class UserService:

    @staticmethod
    def get_all_users():
        users = list(current_app.db.active_user.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return users
