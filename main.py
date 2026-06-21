from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


posts:list[dict] = [
  {
    "id": 1,
    "author": "Alice Johnson",
    "title": "Introduction to Artificial Intelligence",
    "content": "Artificial Intelligence (AI) is transforming industries by enabling machines to learn from data, recognize patterns, and make decisions with minimal human intervention.",
    "date_posted": "2026-06-15T09:30:00Z"
  },
  {
    "id": 2,
    "author": "Michael Chen",
    "title": "Getting Started with Python",
    "content": "Python is one of the most beginner-friendly programming languages due to its simple syntax and extensive ecosystem of libraries for web development, automation, and data science.",
    "date_posted": "2026-06-16T14:45:00Z"
  },
  {
    "id": 3,
    "author": "Sophia Williams",
    "title": "Understanding Machine Learning",
    "content": "Machine learning is a subset of AI where algorithms improve their performance by learning from historical data instead of being explicitly programmed.",
    "date_posted": "2026-06-17T11:20:00Z"
  },
  {
    "id": 4,
    "author": "David Kumar",
    "title": "Benefits of Cloud Computing",
    "content": "Cloud computing provides scalable infrastructure, cost savings, high availability, and easier deployment of applications across the globe.",
    "date_posted": "2026-06-18T08:10:00Z"
  },
  {
    "id": 5,
    "author": "Emma Rodriguez",
    "title": "Data Visualization Best Practices",
    "content": "Effective data visualization focuses on clarity, simplicity, and selecting the appropriate chart type to communicate insights to stakeholders.",
    "date_posted": "2026-06-19T16:55:00Z"
  },
  {
    "id": 6,
    "author": "Rahul Mehta",
    "title": "Building REST APIs with FastAPI",
    "content": "FastAPI is a modern Python framework that simplifies API development with automatic validation, interactive documentation, and excellent performance.",
    "date_posted": "2026-06-20T10:40:00Z"
  },
  {
    "id": 7,
    "author": "Olivia Brown",
    "title": "The Rise of Generative AI",
    "content": "Generative AI models can create text, images, audio, and code, making them valuable tools for content creation, software development, and research.",
    "date_posted": "2026-06-21T07:15:00Z"
  }
]



# Route
@app.get("/", include_in_schema=False)  #decorator
@app.get("/posts",include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts})


@app.get("/api/posts")
def get_posts():
    return posts