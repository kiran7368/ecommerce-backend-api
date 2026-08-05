from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.order_service import (
    place_order,
    get_orders,
    get_order_details,
    cancel_order
)

order_bp = Blueprint(
    "order",
    __name__,
    url_prefix="/api/orders"
)


@order_bp.route("/", methods=["POST"])
@jwt_required()
def create_order():

    user_id = int(get_jwt_identity())

    return place_order(user_id)
@order_bp.route("/", methods=["GET"])
@jwt_required()
def order_history():

    user_id = int(get_jwt_identity())

    return get_orders(user_id)
@order_bp.route("/<int:order_id>", methods=["GET"])
@jwt_required()
def single_order(order_id):

    user_id = int(get_jwt_identity())

    return get_order_details(user_id, order_id)
@order_bp.route("/<int:order_id>/cancel", methods=["PUT"])
@jwt_required()
def cancel(order_id):

    user_id = int(get_jwt_identity())

    return cancel_order(user_id, order_id)