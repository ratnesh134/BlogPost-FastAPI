from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
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


@app.get("/",include_in_schema=False)
@app.get("/posts",include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html"
                                      ,{"posts":posts,"title":"Home"})


@app.get("/api/posts")
def get_posts():
    return posts

