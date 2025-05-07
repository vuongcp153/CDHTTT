from flask import current_app

class UserService:

    @staticmethod
    def get_all_users():
        users = list(current_app.db.active_user.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return users

    @staticmethod
    def match_user_by_preferences(preferences):
        age_range = preferences.get("age_range", [18, 99])
        target_gender = preferences.get("target_gender", [])
        target_ethnicity = preferences.get("target_ethnicity", [])

        # ✅ Lọc theo data.age và status
        query = {
            "data.age": {"$gte": age_range[0], "$lte": age_range[1]},
            "status": "waiting"
        }

        candidates = list(current_app.db.active_user.find(query))

        def compute_score(user):
            score = 0
            data = user.get("data", {})
            if target_gender and data.get("gender") in target_gender:
                score += 1
            if target_ethnicity and data.get("ethnicity") in target_ethnicity:
                score += 1
            return score

        scored = [(user, compute_score(user)) for user in candidates]
        scored = sorted(scored, key=lambda x: x[1], reverse=True)

        if not scored or scored[0][1] == 0:
            return {"message": "Không tìm thấy người phù hợp"}

        best_match = scored[0][0]
        best_match["_id"] = str(best_match["_id"])
        return best_match
