"""
Starter code for the Mini Blog API assignment.

Complete the API by adding the required routes, validation, and error handling
as described in the README.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(
    title="Mini Blog API",
    description="A simple blog API built with FastAPI",
    version="1.0.0",
)


class BlogPost(BaseModel):
    """Represents a blog post in the in-memory database."""
    title: str = Field(..., min_length=3)
    author: str = Field(..., min_length=2)
    content: str = Field(..., min_length=10)
    published: bool = True
    created_at: Optional[datetime] = None


posts: List[dict] = []


# TODO: Task 1 - Create the initial app structure and data model
# Add the root route and set up the in-memory post list


# TODO: Task 2 - Add GET endpoints
# Implement GET /posts and GET /posts/{post_id}


# TODO: Task 3 - Add POST and PUT endpoints with validation
# Create new posts and update existing posts with proper error handling


@app.get("/")
def read_root():
    """Welcome message for the API."""
    return {"message": "Welcome to the Mini Blog API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
