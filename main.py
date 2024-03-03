from fastapi import FastAPI
import uvicorn
from app_1 import app_1

app = FastAPI()
app.mount("/flask_fast_hw/", app_1)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=False)