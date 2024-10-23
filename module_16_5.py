#  module_16_5

from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int = None  # номер пользователя (int)
    username: str   # имя пользователя (str)
    age: int        # возраст пользователя (int)

users = []


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html",  {"request": request, "users": users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user_id = int(user_id)
    user_index = await find_user_id(user_id)
    if user_index < 0:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_index]})

@app.post('/user/{username}/{age}')
async def create_user(user: User = Body()) -> User:
    if len(users) == 0:
        new_user_id = 1
    else:
        new_user_id = users[-1].id + 1
    user.id = new_user_id
    users.append(user)
    return user

async def find_user_id(user_id: int) -> int:
    for usindex, user in enumerate(users):
        if user.id == user_id:
            return usindex
    return -1

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, user: User = Body()) -> User:
    user_index = await find_user_id(user_id)
    if user_index < 0:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        users[user_index].username = user.username
        users[user_index].age = user.age
        return users[user_index]

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    user_index = await find_user_id(user_id)
    if user_index < 0:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        user = users.pop(user_index)
        return user
