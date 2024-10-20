#  module_16_3

from fastapi import FastAPI, Path, HTTPException
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
    users[str(current_index)] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='75')],
                        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                      example='tiger')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    required_key = str(user_id)
    if required_key in users:   # Только если пользователь по искомому ключу найден в базе
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    else:  # KeyError не возникнет, а мы хотим именно ОБНОВИТЬ существующую запись
        raise HTTPException(status_code=404, detail=f"Not updated. User {user_id} was not found.")
    return f"The user {user_id} is registered (updated)."

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='75')]) -> str:
    try:
        users.pop(str(user_id))
    except KeyError:
        raise HTTPException(status_code=404, detail=f"User {user_id} was not found")
    return f"The user {user_id} is deleted"
