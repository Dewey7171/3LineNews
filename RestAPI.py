from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uvicorn
import pymysql
import sql_auth

app = FastAPI()
sql = sql_auth.app


#------------------Class 선언 부분------------------
class addNews(BaseModel):
    name : Optional[str]
    link : Optional[str]

class dbconn:

    # dbconn을 호출하면 맨 처음 나오는 DB연결 기본 함수
    def __init__(self,dbname:str):
        self.connect = pymysql.Connect(
            db=dbname,
            host=sql['host'],
            user=sql['user'],
            password=sql['password'],
            charset=sql['charset'],
            port=55222)

    # DB를 연결해 이용하기 위한 커서 연결 함수
    def conn_cursor (self):
        cur = self.connect.cursor(pymysql.cursors.DictCursor)
        return cur

    # DB를 커밋하는 함수
    def conn_commit(self):
        commit = self.connect.commit()
        return commit
    # DB를 닫는 함수
    def conn_close(self):
        close = self.connect.close()
        return close

connect_cursor = dbconn('News')
develop_cursor = connect_cursor.conn_cursor()


#------------------Class 선언 부분------------------


#-------------------Api 실행 부분-------------------

# 뉴스 리스트 호출
@app.get("/newslist")
async def Newslist():
    news_link_search = "SELECT * FROM news_link"

    develop_cursor.execute(news_link_search)
    newslist = develop_cursor.fetchall()

    connect_cursor.conn_commit()
    connect_cursor.conn_close()

    return newslist


# db에 새로운 링크 집어 넣는 곳
@app.post("/addnews")
async def UpdateNews(addnews : addNews):
    new_News = []
    updates =" INSERT INTO news_link VALUES(default,%s,%s)"
    add_new_Data = dict(addnews)

    new_News.append(add_new_Data['name'])
    new_News.append(add_new_Data['link'])

    develop_cursor.execute(updates,new_News)
    connect_cursor.conn_commit()
    connect_cursor.conn_close()

    return HTTPException(status_code=200, detail="SUCCESS INSERT DATA")

# 뉴스 이름별로
@app.get("/news/{newsname}")
async def News(newsname: str):

    findDB = "SELECT * FROM newdata WHERE newsname ="+f'\'{newsname}\''
    develop_cursor.execute(findDB)
    SelectNews = develop_cursor.fetchall()

    return SelectNews

# 뉴스 날짜별로
@app.get("/date/{date}")
async def News(date: str):

    findDATE = f"SELECT * FROM newdata WHERE DATE(recordtime) =" +f'\'{date}\''
    develop_cursor.execute(findDATE)

    SelectNews = develop_cursor.fetchall()
    return SelectNews

@app.get("/")
async def main():
    main = "fastapi 메인페이지 입니다."
    return main


#-------------------Api 실행 부분-------------------
if __name__ == '__main__':
    uvicorn.run(app)
