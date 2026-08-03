# 🛒 E-Commerce API

## 🚀 Project Overview
This is a robust and scalable E-commerce backend API built with **FastAPI**. It provides a comprehensive set of endpoints for managing users, products, categories, shopping carts, and orders. The application uses **PostgreSQL** for data persistence and **SQLAlchemy** as the ORM, featuring secure JWT-based authentication.

## ✨ Features
- **User Management & Authentication**: User registration, login, and secure JWT token-based authentication.
- **Product Management**: CRUD operations for products.
- **Category Management**: Organizing products into categories.
- **Shopping Cart**: Add, update, and remove items from the shopping cart.
- **Order Processing**: Checkout process and order history tracking.
- **Health Checks**: API endpoint to monitor application health.

## 🛠️ Tech Stack
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (python-jose, passlib, bcrypt)
- **Data Validation**: Pydantic
- **Server**: Uvicorn

## 📂 Folder Structure
```text
m:\project\e-commerce-practise-project\
├── app/
│   ├── api/            # API routers (endpoints)
│   ├── core/           # Core configurations (security, config)
│   ├── db/             # Database connection and session management
│   ├── dependencies/   # FastAPI dependencies (e.g., get_db, auth)
│   ├── models/         # SQLAlchemy database models
│   ├── schemas/        # Pydantic schemas for request/response validation
│   ├── services/       # Business logic layer
│   ├── main.py         # FastAPI application entry point
│   └── requirements.txt# Project dependencies
├── .env                # Environment variables
└── .gitignore
```

## ⚙️ Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository_url>
   cd e-commerce-practise-project
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r app/requirements.txt
   ```

## 🔑 Environment Variables
Create a `.env` file in the root directory and add the following variables:

```env
DATA_BASE_URL=postgresql://<user>:<password>@<host>:<port>/<db_name>
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
```

## ▶️ Running the Project

To start the development server, navigate to the `app` directory and run `uvicorn`:

```bash
cd app
uvicorn main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

## 📖 API Documentation (/docs)
FastAPI automatically generates interactive API documentation. Once the server is running, you can access:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🗄️ Database Schema
The database consists of the following core entities:
- **Users**: Stores user credentials and profile information.
- **Products**: Stores product details (name, description, price, stock).
- **Categories**: Product classification.
- **Carts & Cart Items**: Temporary storage for items users intend to purchase.
- **Orders & Order Items**: Finalized purchases and their details.

*(Detailed relationships are managed via SQLAlchemy models in `app/models/`)*

## 📌 Future Improvements
- [ ] Add payment gateway integration (e.g., Stripe, PayPal).
- [ ] Implement email notifications for order confirmations.
- [ ] Advanced filtering for products.
- [ ] Dockerize the application for easier deployment.
- [ ] Write unit and integration tests using pytest.

## 👨💻 Author
**Madhan**