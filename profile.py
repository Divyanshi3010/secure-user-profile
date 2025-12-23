from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity
from utils.jwt_utils import token_required
from models import User
from utils.encryption import decrypt
from config import Config

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
@token_required
def profile():
    user = User.query.get(get_jwt_identity())
    return jsonify(
        email=user.email,
        aadhaar=decrypt(user.aadhaar_encrypted, Config.AES_SECRET_KEY)
    )