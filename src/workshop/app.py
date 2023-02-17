import uvicorn
from fastapi import FastAPI
from settings import settings
app = FastAPI()


@app.get('/{name}')
def greet(name: str):
    return {'message': f'Hello, {name}'}


#
#
if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
