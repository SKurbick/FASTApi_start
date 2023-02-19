import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.workshop.settings import settings
from src.workshop.api import router

app = FastAPI()
app.include_router(router)

# @app.get('/{name}')
# def greet(name: str):
#     return {'message': f'Hello, {name}'}
# второй вариант вывода данных используя html разметку
#         html_content = "<h2>Hello METANIT.COM!</h2>"
#         return HTMLResponse(content=html_content)
# @app.get('/')
# def root():
#     return {'message': 'Hello!'}


# в консоли uvicorn main:app --reload
# main указывает на название модуля, которое по умолчанию совпадает с названием файла - main
# app указывает на объект приложения, созданный в строке app = FastAPI()
# --reload позволяет отслеживать изменения в файлах исходного кода и автоматически перезапускать проект
