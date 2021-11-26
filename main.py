from apis import RestAPI
from fastapi import FastAPI


def include_router(app):
    app.include_router(RestAPI.router, prefix="/main")


def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()