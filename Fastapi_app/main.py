from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts:list[dict] = [
    {
        "id": 1,
        "title": "First Post from me guys ",
        "content": "This is the content of the first post.",
        "date posted": "28th October 2026",
    },
    
    
    {
            "id": 2,
            "title": "Random Post from me guys ",
            "content": "This is the content of another post.",
            "date posted":"29th October 2026",
        },
]

@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse, include_in_schema=False)

def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
