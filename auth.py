from flask import Blueprint, request, jsonify
from models import db, User
from utils.encryption import encrypt
from config import Config

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print("REGISTER PAYLOAD:", data)

    if not data:
        return jsonify(error="Invalid JSON"), 400

    if not data.get("email") or not data.get("password") or not data.get("aadhaar"):
        return jsonify(error="All fields are required"), 400

    try:
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            return jsonify(error="User already exists"), 409

        new_user = User(email=data["email"])
        new_user.set_password(data["password"])
        new_user.aadhaar_encrypted = encrypt(
            data["aadhaar"], Config.AES_SECRET_KEY
        )

        db.session.add(new_user)
        db.session.commit()

        print("USER INSERTED:", new_user.email)
        return jsonify(msg="User registered successfully"), 201

    except Exception as e:
        db.session.rollback()
        print("REGISTRATION ERROR:", e)
        return jsonify(error=str(e)), 500
