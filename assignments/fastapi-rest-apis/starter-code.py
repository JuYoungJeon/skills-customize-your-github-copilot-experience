"""
Starter code for Building REST APIs with FastAPI Assignment

Complete this API by adding the required endpoints and functionality
as specified in the assignment README.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Learning API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)

# Define a Pydantic model for request/response data
class Item(BaseModel):
    """Model for an item in our API"""
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True


# TODO: Task 1 - Create GET endpoints
# Add at least two GET endpoints that return JSON data
# Example: GET /items and GET /items/{item_id}


# TODO: Task 2 - Create POST endpoints
# Add a POST endpoint that accepts Item data and returns it


# TODO: Task 3 - Add query parameters and error handling
# Extend endpoints with query parameters and proper error handling


# Root endpoint (bonus - already implemented)
@app.get("/")
def read_root():
    """Welcome endpoint - returns a greeting"""
    return {"message": "Welcome to the Learning API!"}


if __name__ == "__main__":
    import uvicorn
    # Run the API with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
