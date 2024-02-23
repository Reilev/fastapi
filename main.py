from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

# request Get method url: "/"

@app.get("/")
async def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post":  f"title {payLoad['title']} content: {payLoad['content']}"}