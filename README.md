# OreRestaurant

OreRestaurant is a backend system built with Flask and SQLite to manage restaurant operations, including user authentication, menu management, and order processing. This project provides RESTful API endpoints for different user actions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features

- User Registration and Authentication
- JWT Token-Based Authentication
- Menu Management by Staff
- Order Placement by Customers
- Role-Based Access Control

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/OreRestaurant.git
   cd OreRestaurant
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables:**

   Create a `.env` file in the root directory and add the following environment variables:

   ```env
   SECRET_KEY=your_secret_key
   MONGO_URI=your_mongo_db_uri
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

2. **Configuration Classes:**

   The `config.py` file contains configuration classes for different environments (development, testing, production). You can modify them as needed.

## Running the Application

1. **Set the Flask environment:**

   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   ```

   On Windows:

   ```bash
   set FLASK_APP=app
   set FLASK_ENV=development
   ```

2. **Run the Flask application:**

   ```bash
   flask run
   ```

## Running Tests

1. **Ensure the virtual environment is activated.**

2. **Run the tests using unittest:**

   ```bash
   python -m unittest discover -s app/tests
   ```

## API Endpoints

### Authentication

- **Register a new user:**

  ```
  POST /auth/register
  ```

  **Request Body:**

  ```json
  {
      "username": "string",
      "password": "string",
      "role": "string"
  }
  ```

- **Login:**

  ```
  POST /auth/login
  ```

  **Request Body:**

  ```json
  {
      "username": "string",
      "password": "string"
  }
  ```

### Menu

- **Get menu items:**

  ```
  GET /menu
  ```

- **Add a new menu item (Staff only):**

  ```
  POST /menu
  ```

  **Request Body:**

  ```json
  {
      "name": "string",
      "description": "string",
      "price": "number",
      "category": "string"
  }
  ```

### Orders

- **Place a new order (Customer only):**

  ```
  POST /orders
  ```

  **Request Body:**

  ```json
  {
      "items": "string"
  }
  ```

- **Get customer orders:**

  ```
  GET /orders
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


---

