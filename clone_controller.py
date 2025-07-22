import os
import subprocess

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class CloneRequest(BaseModel):
    repo_url: str


@app.post("/clone-repo")
def clone_repo(request: CloneRequest):
    repo_url = request.repo_url
    target_dir = "cloned_repos"
    os.makedirs(target_dir, exist_ok=True)
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    clone_path = os.path.join(target_dir, repo_name)
    if os.path.exists(clone_path):
        raise HTTPException(status_code=400, detail="Repository already cloned.")
    try:
        subprocess.run(["git", "clone", repo_url, clone_path], check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Git clone failed: {e}")
    return {"message": f"Repository cloned to {clone_path}"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
