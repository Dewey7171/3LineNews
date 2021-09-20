from typing import Optional

import pymysql
import uvicorn
from pydantic import BaseModel

import sql_auth

from starlette.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from feed_parser import feed

app = FastAPI()

#------------------Mysql 설정 부분------------------
sql = sql_auth.app


class dbconn:

    # dbconn을 호출하면 맨 처음 나오는 DB연결 기본 함수
    def __init__(self,dbname:str):
        self.connect = pymysql.Connect(
            db=dbname,
            host=sql['host'],
            user=sql['user'],
            password=sql['password'],
            charset=sql['charset'])

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




connect_cursor = dbconn('developer')
develop_cursor = connect_cursor.conn_cursor()

search = "SELECT * FROM news_link"
develop_cursor.execute(search)
result = develop_cursor.fetchall()

#------------------Mysql 설정 부분------------------

#------------------Class 선언 부분------------------
class addNews(BaseModel):
    name : Optional[str]
    link : Optional[str]
#------------------Class 선언 부분------------------


#-------------------Api 실행 부분-------------------
@app.get("/news_list")
async def Newslist():
    newslist_db = "SELECT name,link FROM news_link "
    develop_cursor.execute(newslist_db)
    newslist = develop_cursor.fetchall()

    connect_cursor.conn_commit()
    connect_cursor.conn_close()

    return newslist


# db에 새로운 링크 집어 넣는 곳
@app.post("/addnews")
async def UpdateNews(addnews : addNews):

    new_News = []
    # 근데 여기에 rss 링크가 아닌 일반 링크가 들어오면 망치는데 어떡하지?
    # 이 작업은 어디서 해야될까? feed_parser에서 진행해야 될 것으로 보이긴함

    updates =" INSERT INTO news_link VALUES(%s,%s,%s)"
    add_new_Data = dict(addnews)

    new_News.append(len(result)+1)
    new_News.append(add_new_Data['name'])
    new_News.append(add_new_Data['link'])

    develop_cursor.execute(updates,new_News)


    return HTTPException(status_code=200, detail="SUCCESS INSERT DATA")

@app.get("/{news_name}")
async def News(news_name: str):

    for i in result:
        newsNameData = i['name']
        if news_name.lower() == newsNameData:
            b = iter(i)
            c = next(b)

            if c.find(newsNameData):
                rss_url = i['link']
            else:
                raise HTTPException(status_code=404, detail="Notfound Link Please recheck URL")

    News = feed(rss_url)
    return JSONResponse(News)
#-------------------Api 실행 부분-------------------

if __name__ == '__main__':
    uvicorn.run(app)

