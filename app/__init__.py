from flask import Flask
from flasgger import Swagger

from app.config import Config
from app.extensions import db, migrate, jwt, bcrypt

from app.models.user import User
from app.routes.auth import auth_bp
from app.models.category import Category
from app.routes.category import category_bp
from app.models.product import Product
from app.routes.product import product_bp
from app.models.cart import CartItem
from app.routes.cart import cart_bp
from app.models.order import Order
from app.models.order_item import OrderItem
from app.routes.order import order_bp



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    Swagger(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)

    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "Welcome to E-Commerce Backend API"
        }

    return app