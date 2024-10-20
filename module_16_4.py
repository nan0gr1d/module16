#  module_16_4

from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

class User(BaseModel):
    id: int = None  # номер пользователя (int)
    username: str   # имя пользователя (str)
    age: int        # возраст пользователя (int)

users = []

@app.get('/users')
async def get_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(user: User = Body()) -> User:
    user.id = len(users)
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, user: User = Body()) -> User:
    try:
        edit_user = users[user_id]
        edit_user.username = user.username
        edit_user.age = user.age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        user = users.pop(user_id)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
