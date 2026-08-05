from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.schemas.cart_schema import CartSchema
from app.services.cart_service import (
    add_to_cart,
    get_cart
)

cart_bp = Blueprint(
    "cart",
    __name__,
    url_prefix="/api/cart"
)

cart_schema = CartSchema()


@cart_bp.route("/", methods=["POST"])
@jwt_required()
def add_cart():

    try:

        data = cart_schema.load(request.get_json())

        user_id = int(get_jwt_identity())

        return add_to_cart(
            user_id,
            data["product_id"],
            data["quantity"]
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400
@cart_bp.route("/", methods=["GET"])
@jwt_required()
def view_cart():

    user_id = int(get_jwt_identity())

    return get_cart(user_id)   