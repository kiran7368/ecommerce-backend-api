from flask import Blueprint
from app.extensions import db
from app.models.category import Category
from app.models.product import Product

seed_bp = Blueprint("seed", __name__, url_prefix="/api")

@seed_bp.route("/seed", methods=["GET"])
def seed():

    if Product.query.count() > 0:
        return {
            "status": "success",
            "message": "Database already seeded"
        }

    electronics = Category(name="Electronics")

    db.session.add(electronics)
    db.session.commit()

    products = [

        Product(
            name="iPhone 16 Pro",
            description="Apple flagship smartphone",
            price=129999,
            stock=20,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        ),

        Product(
            name="MacBook Air M4",
            description="Apple Laptop",
            price=149999,
            stock=15,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        ),

        Product(
            name="Apple Watch Ultra",
            description="Premium Smart Watch",
            price=89999,
            stock=30,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        )

    ]

    db.session.add_all(products)
    db.session.commit()

    return {
        "status": "success",
        "message": "Database seeded successfully"
    }
