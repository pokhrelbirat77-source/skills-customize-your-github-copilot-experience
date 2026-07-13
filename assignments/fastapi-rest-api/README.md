# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a simple REST API using FastAPI and Pydantic models to practice endpoint routing, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Define the API Application

#### Description

Create a FastAPI application and add routes for managing basic item data.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define the routes `GET /items`, `GET /items/{item_id}`, and `POST /items`
- Return JSON responses from each endpoint

### 🛠️ Create Pydantic Models

#### Description

Use Pydantic models to validate incoming request data and structure the API output.

#### Requirements
Completed program should:

- Define a Pydantic model for item input with `name`, `description`, and `price`
- Define a response model for returned items
- Validate the `POST /items` request body with the input model

### 🛠️ Manage Item Data and Responses

#### Description

Implement simple in-memory storage and error handling for the item API.

#### Requirements
Completed program should:

- Store items in a Python data structure
- Assign a unique `item_id` to each created item
- Return created item data after `POST /items`
- Handle missing items with a 404 error for `GET /items/{item_id}`
