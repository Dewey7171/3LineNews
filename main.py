from View import RestAPI
from fastapi import FastAPI
from Model import db_install

def include_router(app):
    app.include_router(RestAPI.router, prefix="/news")

def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_install.table_install()
app = start_application()