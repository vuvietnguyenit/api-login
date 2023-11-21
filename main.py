

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from src.db import get_user, get_user_by_id, insert_user
from src.schema import User, UserLogin
from src.utils import hashmd5


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/ping")
async def root():
    return {"message": "Hello page"}


@app.post("/login")
async def login(user: UserLogin):
    password = hashmd5(user.password)
    payload = {
        "username": user.username,
        "password": password,
    }
    user_data = get_user(user=payload)
    if not user_data:
        return JSONResponse(content={"message": "Login failed"}, status_code=401)
    return JSONResponse(content={"message": "Login success"}, status_code=200)


@app.post("/register")
async def register(user: User):
    try:
        password = hashmd5(user.password)
        userdata = {
            "username": user.username,
            "password": user.password,
            "location": user.location,
            "description": user.description,
            "age": user.age,
            "password": password
        }
        insert_user(user=userdata)
        return JSONResponse(content={"message": f"Create user with username: {user.username} successful"}, status_code=201)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=400)


@app.get("/user/{user_id}")
async def view_user(user_id: str):
    if not user_id:
        return JSONResponse(content={"message": "user_id is not empty"}, status_code=401)
    user = get_user_by_id(user_id)
    userdata = {
        "username": user.get("username"),
        "fullname": user.get("fullname"),
        "location": user.get("location"),
        "description": user.get("description"),
        "age": user.get('age'),
    }
    return JSONResponse(content={"userdata": userdata}, status_code=200)


@app.post("/delete_user")
async def view_user(user: UserLogin):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                reload=True, log_level="debug")
