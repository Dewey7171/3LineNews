from View import api_get,api_post,api_delete
from fastapi import FastAPI
from Model import db_install

def include_router(app):
    app.include_router(api_get.router, prefix="/news")
    app.include_router(api_post.router, prefix="/news")
    app.include_router(api_delete.router, prefix="/news")

def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_install.table_install()
app = start_application()
