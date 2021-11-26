from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from sqlalchemy import MetaData, Table
from connection_db import db_connection,db_class

Newdata = db_class.Newdata
Newslink = db_class.Newslink
metadata = MetaData()
engine = db_connection.engineconn()
session = engine.sessionmaker()
router = APIRouter()

class Addnews(BaseModel):
    name: str
    link: str

#-------------------Api 실행 부분-------------------

# 뉴스 내용 전체 호출
@router.get('/news/all', tags=["main"])
async def newsdata():
    table = Table('newdata', metadata, autoload=True, autoload_with=engine.engine)
    newdata = session.query(table).all()
    session.close()
    return newdata

# 뉴스 사이트 전체 호출
@router.get('/newslist', tags=["main"])
async def news_list():
    table1 = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)
    newslist = session.query(table1).all()
    session.close()
    return newslist

# 뉴스 사이트 추가
@router.post('/newslist', tags=["main"])
async def news_list(add : Addnews):
    addMemo = Newslink(name=add.name,link=add.link)
    session.add(addMemo)

    try:
        session.commit()
        session.close()
        result = HTTPException(status_code=200, detail="Add Complete")

    except:
        result = HTTPException(status_code=404, detail="Add Failed")

    return result

# 뉴스 사이트 별 조회
@router.get('/news/site/{news}', tags=["main"])
async def news_name(news : str):
    result = session.query(Newdata).filter(Newdata.name == news).all()

    if result == []:
        result = HTTPException(status_code=404, detail="제공되는 뉴스가 존재하지 않습니다.")
    else:
        session.close()

    return result

# 뉴스 날짜별 조회
@router.get('/news/date/{date}', tags=["main"])
async def qwe(date : str):
    result = session.query(Newdata).filter(Newdata.data.comparator['date'] == date).all()

    if result == []:
        result = HTTPException(status_code=404, detail="해당 날짜에 존재하는 데이터가 없거나 날짜 형식을 20XX-XX-XX로 변경하세요")
    else:
        session.close()
    return result

