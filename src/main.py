# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .analysis import get_most_complex_repo

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="templates"), name="static")

# Serve the main HTML file at the root URL
@app.get("/")
def serve_index():
    return FileResponse("templates/index.html")

@app.get("/analyze")
async def analyze_user_repos(github_url: str):
    try:
        # Extract GitHub username from URL
        username = github_url.split("github.com/")[-1]
        result = await get_most_complex_repo(username)
        return {"most_complex_repo": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
