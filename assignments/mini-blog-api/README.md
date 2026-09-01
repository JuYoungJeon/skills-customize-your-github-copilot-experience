# 📘 Assignment: Mini Blog API

## 🎯 Objective

Build a small blog application backend using FastAPI. In this assignment, you'll design a simple data model, create REST endpoints for reading and creating posts, and practice handling JSON requests and validation in a realistic web API project.

## 📝 Tasks

### 🛠️ Create the Blog Post Model

#### Description
Set up the FastAPI app and define the structure for blog posts. Your goal is to create a clear model for the data your API will manage.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a blog post data model with fields like `title`, `author`, `content`, and `published`
- Use Pydantic validation to ensure required fields are present and properly formatted
- Include an in-memory store for posts so the API can add and retrieve data during the session
- Return a welcome message at the root route (`/`)

### 🛠️ Add GET Endpoints for Reading Posts

#### Description
Create endpoints that let clients list all blog posts and fetch one specific post by its ID. This helps you practice route design and working with JSON data.

#### Requirements
Completed program should:

- Create a `GET /posts` endpoint that returns all stored posts
- Create a `GET /posts/{post_id}` endpoint that returns a single post by ID
- Return a JSON response for each request
- Use a numeric or string ID system consistently throughout the app
- Return a clear 404 error when a requested post does not exist

### 🛠️ Add Create, Update, and Error Handling

#### Description
Extend the API so it can create new posts and handle invalid input with meaningful responses. This is where students practice real-world API behavior.

#### Requirements
Completed program should:

- Create a `POST /posts` endpoint that accepts a new blog post
- Validate incoming data before storing it
- Return the created post with a success response after it is added
- Add an `PUT /posts/{post_id}` endpoint to update an existing post
- Return appropriate HTTP error codes for invalid requests or missing posts
- Include clear messages such as "Post not found" or "Title is required"

