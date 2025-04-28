from datetime import datetime

class User:
    def __init__(self,session, data, preference, status):
        self.session = session
        self.data = data
        self.preference = preference
        self.last_activity = datetime.now()
        self.status = status

    def to_dict(self):
        return {
            "session_id": self.session,
            "data": self.data,
            "preference": self.preference,
            "last_activity": self.last_activity,
            "status": self.status
        }
