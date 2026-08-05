from app.models.user import User
from app.extensions import db, bcrypt


def register_user(full_name, email, password):

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {
            "status": "error",
            "message": "Email already exists"
        }, 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(
        full_name=full_name,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return {
        "status": "success",
        "message": "User registered successfully"
    }, 201
from flask_jwt_extended import create_access_token


def login_user(email, password):

    user = User.query.filter_by(email=email).first()

    if not user:
        return {
            "status": "error",
            "message": "Invalid email or password"
        }, 401

    if not bcrypt.check_password_hash(user.password, password):
        return {
            "status": "error",
            "message": "Invalid email or password"
        }, 401

    access_token = create_access_token(identity=str(user.id))

    return {
        "status": "success",
        "message": "Login successful",
        "access_token": access_token
    }, 200
def get_profile(user):

    return {
        "status": "success",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at
        }
    }, 200