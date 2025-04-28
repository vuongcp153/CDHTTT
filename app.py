from flask import Flask
from pymongo import MongoClient
from config import Config
from blueprints.usersBP import users_bp


app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(app.config['MONGO_URI'])
app.db = client[app.config['DB_NAME']]
print("MongoDB connected")

app.register_blueprint(users_bp, url_prefix="/users")
# app.register_blueprint(matches_bp, url_prefix="/matches")

if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    app.run(debug=True, host=host, port=port)
