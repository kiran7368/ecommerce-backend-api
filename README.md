# E-Commerce Backend API

This is a backend project that I built using Flask and PostgreSQL to understand how real-world e-commerce applications work. The project includes user authentication, product management, shopping cart, and order management APIs. It is containerized using Docker and deployed on Render.

## Live Demo

API:
https://ecommerce-backend-api-fj7y.onrender.com

Swagger Documentation:
https://ecommerce-backend-api-fj7y.onrender.com/apidocs/

---

## Features

- User registration and login
- JWT authentication
- User profile API
- Category management
- Product management
- Product search
- Pagination
- Shopping cart
- Place orders
- Swagger API documentation
- Docker support

---

## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-JWT-Extended
- Docker
- Swagger
- Render
- Neon PostgreSQL

---

## Why I Built This Project

I wanted to improve my backend development skills by building a complete REST API from scratch. Instead of creating only CRUD APIs, I tried to include features that are commonly used in real applications like authentication, cart management, order processing, Docker support, and cloud deployment.

This project helped me understand database design, API development, authentication, Docker, and deployment workflows.

---

## Project Structure

```
app/
 ├── models/
 ├── routes/
 ├── services/
 ├── schemas/
 ├── extensions.py

migrations/
run.py
Dockerfile
docker-compose.yml
requirements.txt
```

---

## Run Locally

```bash
git clone https://github.com/kiran7368/ecommerce-backend-api.git

cd ecommerce-backend-api

pip install -r requirements.txt

python run.py
```

---

## Future Improvements

- Admin dashboard APIs
- Product image upload
- Payment gateway integration
- Email notifications
- Unit testing
- CI/CD using GitHub Actions

---

## Author

**Kiran Babu**

GitHub:
https://github.com/kiran7368