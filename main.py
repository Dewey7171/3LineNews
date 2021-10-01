from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from feed_parser import feed

import pymysql
import uvicorn
import sql_auth

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

news_link_search = "SELECT * FROM news_link"
develop_cursor.execute(news_link_search)
news_link_result = develop_cursor.fetchall()

#------------------Mysql 설정 부분------------------


#------------------Class 선언 부분------------------
class addNews(BaseModel):
    name : Optional[str]
    link : Optional[str]
#------------------Class 선언 부분------------------


#-------------------Api 실행 부분-------------------
@app.get("/news_list")
async def Newslist():

    develop_cursor.execute(news_link_search)
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

    updates =" INSERT INTO news_link VALUES(default,%s,%s)"
    add_new_Data = dict(addnews)

    new_News.append(add_new_Data['name'])
    new_News.append(add_new_Data['link'])

    develop_cursor.execute(updates,new_News)
    connect_cursor.conn_commit()
    connect_cursor.conn_close()

    return HTTPException(status_code=200, detail="SUCCESS INSERT DATA")

@app.get("/{news_name}")
async def News(news_name: str):

    for i in news_link_result:
        newsNameData = i['name']
        if news_name.lower() == newsNameData:
            b = iter(i)
            c = next(b)

            if c.find(newsNameData):
                rss_url = i['link']
            else:
                raise HTTPException(status_code=404, detail="Notfound Link Please recheck URL")

    News = feed(rss_url)


    newdata_search = "SELECT * FROM newdata"
    develop_cursor.execute(newdata_search)

    for data in range(0,len(News)):
        datasaver = []
        dataUpdates = " INSERT INTO newdata VALUES(default,%s,%s,%s,%s,default,%s)"
        datasaver.append(News[data]['title'])
        datasaver.append(News[data]['content'])
        datasaver.append(News[data]['url'])
        datasaver.append(news_name)
        datasaver.append(News[data]['date'])
        develop_cursor.execute(dataUpdates, datasaver)

    connect_cursor.conn_commit()
    connect_cursor.conn_close()
    return datasaver

#-------------------Api 실행 부분-------------------

if __name__ == '__main__':
    uvicorn.run(app)

