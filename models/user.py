from datetime import datetime

class User:
    def __init__(self, data, is_matched=False):
        self.data = data
        self.timestamp = datetime.now()
        self.is_matched = is_matched

    def to_dict(self):
        return {
            "data": self.data,
            "timestamp": self.timestamp,
            "is_matched": self.is_matched
        }
