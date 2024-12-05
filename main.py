import uvicorn

from fastapi import FastAPI, HTTPException
from schemas.pydantic_models import ExampleModel

app = FastAPI(
    description="API Docs for General Projects",)


@app.get("/")
async def root():
    return {"message": "General Project"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1995)
