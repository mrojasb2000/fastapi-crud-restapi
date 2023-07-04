from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()
posts = []

# Post model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get("/")
def read_root():
    return {"welcome": "welcome to my REST API"}

@app.get("/posts")
def getPosts():
    return posts

@app.post("/posts")
def create(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())