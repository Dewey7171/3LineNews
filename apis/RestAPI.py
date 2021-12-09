from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import MetaData, Table
from connection_db import db_connection,db_class

Newdata = db_class.Newsdata
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
@router.get('/all', tags=["news"])
async def newsdata():
    try:
        table1 = Table('news_data', metadata, autoload=True, autoload_with=engine.engine)

    except:
        result = JSONResponse(status_code=404, content="해당 테이블이 존재하지 않습니다.")

    else:
        result = session.query(table1).all()

    finally:
        session.close()

    return result

# 뉴스 사이트 전체 호출
@router.get('/newslist', tags=["news"])
async def news_list():
    try:
        table1 = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)

    except:
        result = JSONResponse(status_code=404, content="해당 테이블이 존재하지 않습니다.")

    else:
        result = session.query(table1).all()

    finally:
        session.close()

    return result

# 뉴스 사이트 추가
@router.post('/newslist', tags=["news"])
async def news_list(add : Addnews):
    addMemo = Newslink(name=add.name,link=add.link)
    session.add(addMemo)

    try:
        session.commit()
        session.close()
        result = JSONResponse(status_code=200, content="Add Complete")

    except:
        result = JSONResponse(status_code=404, content="Add Failed")

    return result

# 뉴스 사이트 별 조회
@router.get('/site/{news}', tags=["news"])
async def news_name(news : str):
    result = session.query(Newdata).filter(Newdata.name == news).all()

    if result == []:
        result = JSONResponse(status_code=404, content="제공되는 뉴스가 존재하지 않습니다.")

    else:
        session.close()

    return result

# 뉴스 날짜별 조회
@router.get('/date/{date}', tags=["news"])
async def date(date : str):
    result = session.query(Newdata).filter(Newdata.data.comparator['date'] == date).all()

    if result == []:
        result = JSONResponse(status_code=404, content="해당 날짜에 존재하는 데이터가 없거나 날짜 형식을 20XX-XX-XX로 변경하세요")

    else:
        session.close()

    return result