from View import api_get,api_post,api_delete,api_update
from fastapi import FastAPI
from Model import db_install

# 각 API Endpoint를 라우터로 통합 시켜 작동하게 만드는 부분
def include_router(app):
    app.include_router(api_get.router, prefix="/news")
    app.include_router(api_post.router, prefix="/news")
    app.include_router(api_delete.router, prefix="/news")
    app.include_router(api_update.router, prefix="/news")

# FastAPI의 직접적인 실행 부분을 담당
def start_application():
    app = FastAPI()
    include_router(app)
    return app

# DB에 해당 테이블이 존재하지 않는다면 Class에서 명시한 내용 대로 테이블 생성
db_install.table_install()
app = start_application()