#  module_16_3

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                      example='tiger')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    current_index = int(max(users, key=int)) + 1
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='75')],
                        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                      example='tiger')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='75')]) -> str:
    _ = users.pop(user_id)
    return f"The user {user_id} is deleted"
