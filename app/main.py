from fastapi import FastAPI
from app.api import upload  # import the upload router

app = FastAPI()

# Include the upload route
app.include_router(upload.router)

@app.get("/")
def read_root():
    return {"message": "AI-FakeDetect API is running."}
