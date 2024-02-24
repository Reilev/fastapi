from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(payLoad)
    return {"new_post":  f"title {payLoad['title']} content: {payLoad['content']}"}
#title str, content str