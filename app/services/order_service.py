from app.extensions import db
from app.models.cart import CartItem
from app.models.order import Order
from app.models.order_item import OrderItem


def place_order(user_id):

    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return {
            "status": "error",
            "message": "Cart is empty"
        }, 400

    grand_total = 0

    for item in cart_items:
        grand_total += item.quantity * item.product.price

    order = Order(
        user_id=user_id,
        total_amount=grand_total
    )

    db.session.add(order)
    db.session.flush()

    for item in cart_items:

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )

        db.session.add(order_item)

    CartItem.query.filter_by(user_id=user_id).delete()

    db.session.commit()

    return {
        "status": "success",
        "message": "Order placed successfully",
        "order_id": order.id,
        "total_amount": grand_total
    }, 201
def get_orders(user_id):

    orders = Order.query.filter_by(user_id=user_id).order_by(Order.created_at.desc()).all()

    result = []

    for order in orders:

        result.append({
            "order_id": order.id,
            "total_amount": order.total_amount,
            "status": order.status,
            "created_at": order.created_at
        })

    return {
        "status": "success",
        "orders": result
    }, 200
def get_order_details(user_id, order_id):

    order = Order.query.filter_by(
        id=order_id,
        user_id=user_id
    ).first()

    if not order:
        return {
            "status": "error",
            "message": "Order not found"
        }, 404

    items = []

    for item in order.items:

        items.append({
            "product": item.product.name,
            "price": item.price,
            "quantity": item.quantity,
            "subtotal": item.price * item.quantity
        })

    return {
        "status": "success",
        "order": {
            "id": order.id,
            "status": order.status,
            "total_amount": order.total_amount,
            "created_at": order.created_at,
            "items": items
        }
    }, 200
def cancel_order(user_id, order_id):

    order = Order.query.filter_by(
        id=order_id,
        user_id=user_id
    ).first()

    if not order:

        return {
            "status": "error",
            "message": "Order not found"
        }, 404

    if order.status != "Pending":

        return {
            "status": "error",
            "message": "Only pending orders can be cancelled"
        }, 400

    order.status = "Cancelled"

    db.session.commit()

    return {
        "status": "success",
        "message": "Order cancelled successfully"
    }, 200