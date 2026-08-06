from app import create_app
from app.extensions import db
from app.models.category import Category
from app.models.product import Product

app = create_app()

with app.app_context():

    if Category.query.count() == 0:

        electronics = Category(name="Electronics")

        db.session.add(electronics)
        db.session.commit()

        iphone = Product(
            name="iPhone 16 Pro",
            description="Apple flagship smartphone",
            price=129999,
            stock=20,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        )

        macbook = Product(
            name="MacBook Air M4",
            description="Apple Laptop",
            price=149999,
            stock=15,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        )

        watch = Product(
            name="Apple Watch Ultra",
            description="Premium Smart Watch",
            price=89999,
            stock=25,
            image_url="https://placehold.co/400x300",
            category_id=electronics.id
        )

        db.session.add_all([iphone, macbook, watch])
        db.session.commit()

        print("✅ Sample data inserted!")

    else:
        print("Database already has data.")