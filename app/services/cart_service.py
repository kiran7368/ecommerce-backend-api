from app.extensions import db
from app.models.cart import CartItem
from app.models.product import Product


def add_to_cart(user_id, product_id, quantity):

    product = Product.query.get(product_id)

    if not product:

        return {
            "status": "error",
            "message": "Product not found"
        }, 404

    cart = CartItem.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if cart:

        cart.quantity += quantity

    else:

        cart = CartItem(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )

        db.session.add(cart)

    db.session.commit()

    return {
        "status": "success",
        "message": "Product added to cart"
    }, 201
def get_cart(user_id):

    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    result = []

    grand_total = 0

    for item in cart_items:

        subtotal = item.quantity * item.product.price

        grand_total += subtotal

        result.append({

            "id": item.id,

            "product": item.product.name,

            "price": item.product.price,

            "quantity": item.quantity,

            "subtotal": subtotal

        })

    return {

        "status": "success",

        "cart": result,

        "grand_total": grand_total

    }, 200