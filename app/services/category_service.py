from app.extensions import db
from app.models.category import Category


def create_category(name, description):

    category = Category.query.filter_by(name=name).first()

    if category:
        return {
            "status": "error",
            "message": "Category already exists"
        }, 409

    new_category = Category(
        name=name,
        description=description
    )

    db.session.add(new_category)
    db.session.commit()

    return {
        "status": "success",
        "message": "Category created successfully"
    }, 201


def get_categories():

    categories = Category.query.all()

    result = []

    for category in categories:

        result.append({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at
        })

    return {
        "status": "success",
        "categories": result
    }, 200
def update_category(category_id, name, description):

    category = Category.query.get(category_id)

    if not category:
        return {
            "status": "error",
            "message": "Category not found"
        }, 404

    category.name = name
    category.description = description

    db.session.commit()

    return {
        "status": "success",
        "message": "Category updated successfully"
    }, 200


def delete_category(category_id):

    category = Category.query.get(category_id)

    if not category:
        return {
            "status": "error",
            "message": "Category not found"
        }, 404

    db.session.delete(category)
    db.session.commit()

    return {
        "status": "success",
        "message": "Category deleted successfully"
    }, 200