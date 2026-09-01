# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern web APIs using FastAPI, a high-performance Python framework. You'll create endpoints for handling HTTP requests, work with JSON data, and understand REST principles while building a practical API service.

## 📝 Tasks

### 🛠️ Create a Basic API with GET Endpoints

#### Description
Build your first FastAPI application with multiple GET endpoints that return different types of data. Learn how to define routes and return JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define at least two GET endpoints that return different data
- Return JSON responses with appropriate HTTP status codes (200 OK)
- Include route documentation/docstrings for each endpoint
- Use path parameters in at least one endpoint (e.g., `/items/{item_id}`)

### 🛠️ Add POST Endpoints to Handle Data

#### Description
Extend your API with POST endpoints that accept data from clients. Learn how to define request body schemas and validate incoming data.

#### Requirements
Completed program should:

- Define a Pydantic model for request validation
- Create at least one POST endpoint that accepts JSON data
- Validate and process the incoming data
- Return a meaningful response with the processed data
- Test the endpoint with sample requests

### 🛠️ Implement Query Parameters and Error Handling

#### Description
Add advanced features including query parameters for filtering/sorting and proper error handling for invalid requests.

#### Requirements
Completed program should:

- Implement query parameters in at least one endpoint (e.g., `?skip=0&limit=10`)
- Add validation and error handling for invalid inputs
- Return appropriate HTTP error codes (400 Bad Request, 404 Not Found, etc.)
- Provide clear error messages to API clients
- Test edge cases like missing or invalid query parameters
