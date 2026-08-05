from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.user_schema import RegisterSchema, LoginSchema
from app.services.auth_service import (
    register_user,
    login_user,
    get_profile
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

register_schema = RegisterSchema()
login_schema = LoginSchema()


@auth_bp.route("/", methods=["GET"])
def auth_home():
    return jsonify({
        "status": "success",
        "message": "Authentication API is Working 🚀"
    })


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register New User
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            full_name:
              type: string
              example: Kiran Babu
            email:
              type: string
              example: kiran@gmail.com
            password:
              type: string
              example: 12345678

    responses:
      201:
        description: User registered successfully
      400:
        description: Validation Error
    """


    try:

        data = register_schema.load(request.get_json())

        return register_user(
            full_name=data["full_name"],
            email=data["email"],
            password=data["password"]
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400
@auth_bp.route("/login", methods=["POST"])
def login():

    try:

        data = login_schema.load(request.get_json())

        return login_user(
            email=data["email"],
            password=data["password"]
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    return get_profile(user)       