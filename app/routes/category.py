from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.category_schema import CategorySchema
from app.services.category_service import (
    create_category,
    get_categories,
    update_category,
    delete_category
)

category_bp = Blueprint(
    "category",
    __name__,
    url_prefix="/api/categories"
)

category_schema = CategorySchema()


@category_bp.route("/", methods=["GET"])
def all_categories():

    return get_categories()


@category_bp.route("/", methods=["POST"])
def add_category():

    try:

        data = category_schema.load(request.get_json())

        return create_category(
            name=data["name"],
            description=data.get("description")
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400
@category_bp.route("/<int:category_id>", methods=["PUT"])
def edit_category(category_id):

    try:

        data = category_schema.load(request.get_json())

        return update_category(
            category_id,
            data["name"],
            data.get("description")
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400


@category_bp.route("/<int:category_id>", methods=["DELETE"])
def remove_category(category_id):

    return delete_category(category_id)    