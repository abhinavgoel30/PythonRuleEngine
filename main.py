from fastapi import FastAPI
import standing_pose

app = FastAPI()

# Include the routes from endpoints.py
app.include_router(standing_pose.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}





@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}