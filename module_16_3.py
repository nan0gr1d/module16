#  module_16_3

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def get_main_page() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def get_admin_page() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def get_user_number(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID',
                                                       example='75')]) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user/{username}/{age}')
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                      example='tiger')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


"""
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is registered"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}
"""
