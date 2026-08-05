from app.extensions import db
from app.models.product import Product
from app.models.category import Category


def create_product(
    name,
    description,
    price,
    stock,
    image_url,
    category_id
):

    category = Category.query.get(category_id)

    if not category:

        return {
            "status": "error",
            "message": "Category not found"
        }, 404

    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        image_url=image_url,
        category_id=category_id
    )

    db.session.add(product)
    db.session.commit()

    return {
        "status": "success",
        "message": "Product created successfully"
    }, 201
def get_products():

    products = Product.query.all()

    result = []

    for product in products:

        result.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "image_url": product.image_url,
            "category": product.category.name,
            "created_at": product.created_at
        })

    return {
        "status": "success",
        "products": result
    }, 200
def get_product(product_id):

    product = Product.query.get(product_id)

    if not product:
        return {
            "status": "error",
            "message": "Product not found"
        }, 404

    return {
        "status": "success",
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "image_url": product.image_url,
            "category": product.category.name,
            "created_at": product.created_at
        }
    }, 200
from sqlalchemy import or_


def search_products(keyword):

    products = Product.query.filter(

        or_(

            Product.name.ilike(f"%{keyword}%"),

            Product.description.ilike(f"%{keyword}%")

        )

    ).all()

    result = []

    for product in products:

        result.append({

            "id": product.id,

            "name": product.name,

            "description": product.description,

            "price": product.price,

            "stock": product.stock,

            "category": product.category.name

        })

    return {

        "status": "success",

        "products": result

    }, 200
def get_products_paginated(page, per_page):

    pagination = Product.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    result = []

    for product in pagination.items:

        result.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category.name
        })

    return {
        "status": "success",
        "page": pagination.page,
        "total_pages": pagination.pages,
        "total_products": pagination.total,
        "products": result
    }, 200