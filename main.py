from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # to get the response in human readable form not in JSON


app = FastAPI()


post: list[dict] = [
    {
        "id": 1,
        "author": "Ratnesh Kumar",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "February  19th 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is great for web development",
        "content": "I am still learning this framework",
        "date_posted": "February 18th 2026",
    },
]


@app.get("/",response_class=HTMLResponse)
def home():
    return f"<h1>{post[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return post