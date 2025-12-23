from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes.auth import auth_bp
from routes.profile import profile_bp

app = Flask(__name__)
app.config.from_object(Config)

# ✅ FIX: Enable CORS for React frontend
CORS(app, supports_credentials=True)

db.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(profile_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
