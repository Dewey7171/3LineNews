from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from sqlalchemy import MetaData
from Model import db_connection, db_class
from Presenter import pre_request

Newdata = db_class.Newsdata
Newslink = db_class.Newslink
metadata = MetaData()
engine = db_connection.engineconn()
session = engine.sessionmaker()
router = APIRouter()

class Addnews(BaseModel):
    name: Optional[str]
    link: str

#-------------------Api 실행 부분-------------------

# 뉴스 내용 전체 호출
@router.get('/all', tags=["news"])
async def newsdata():
    result = pre_request.pre_get_all()

    return result

# 뉴스 사이트 전체 호출
@router.get('/newslist', tags=["news"])
async def news_list():
    result = pre_request.pre_get_list()

    return result

# 뉴스 사이트 추가
@router.post('/newslist', tags=["news"])
async def news_list(add : Addnews):
    result = pre_request.pre_post_list(add)

    return result

# 뉴스 사이트 별 조회
@router.get('/site/{news}', tags=["news"])
async def news_name(news : str):
    result = pre_request.pre_get_newsdata(news)

    return result

# 뉴스 날짜별 조회
@router.get('/date/{date}', tags=["news"])
async def date(date : str):
    result = pre_request.pre_get_date(date)

    return result
