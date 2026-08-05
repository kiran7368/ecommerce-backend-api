from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.product_schema import ProductSchema
from app.services.product_service import (
    create_product,
    get_products,
    get_product,
    search_products,
    get_products_paginated
)

product_bp = Blueprint(
    "product",
    __name__,
    url_prefix="/api/products"
)

product_schema = ProductSchema()


@product_bp.route("/", methods=["POST"])
def add_product():

    try:

        data = product_schema.load(request.get_json())

        return create_product(
            data["name"],
            data["description"],
            data["price"],
            data["stock"],
            data.get("image_url"),
            data["category_id"]
        )

    except ValidationError as err:

        return jsonify({
            "status": "error",
            "errors": err.messages
        }), 400
@product_bp.route("/", methods=["GET"])
def all_products():

    return get_products()
@product_bp.route("/<int:product_id>", methods=["GET"])
def single_product(product_id):

    return get_product(product_id)
@product_bp.route("/search", methods=["GET"])
def search():

    keyword = request.args.get("name", "")

    return search_products(keyword)
@product_bp.route("/page", methods=["GET"])
def paginate_products():

    page = request.args.get("page", default=1, type=int)

    per_page = request.args.get("limit", default=5, type=int)

    return get_products_paginated(page, per_page)    