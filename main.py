from typing import Optional

import pymysql
import uvicorn
from pydantic import BaseModel

import sql_auth


from starlette.responses import JSONResponse, Response
from fastapi import FastAPI, HTTPException, Form
from feed_parser import feed

# to get a string like this run:
# openssl rand -hex 32

app = FastAPI()


#------------------Mysql 설정 부분------------------
sql = sql_auth.app
conn = pymysql.Connect(
    db=sql['db'],
    host=sql['host'],
    user=sql['user'],
    password=sql['password'],
    charset=sql['charset'])

s = conn.cursor(pymysql.cursors.DictCursor)

search = "SELECT * FROM news_link"
s.execute(search)
result = s.fetchall()
#------------------Mysql 설정 부분------------------

#------------------Class 선언 부분------------------



#------------------Class 선언 부분------------------


#-------------------Api 실행 부분-------------------

@app.get("/news_list")
async def Newslist():
    newslist_db = "SELECT name,link FROM news_link "
    s.execute(newslist_db)
    newslist = s.fetchall()
    return newslist



@app.get("/{news_name}")
async def News(news_name: str):

    for i in result:

        a = i['name']

        if news_name.lower() == a:
            b = iter(i)
            c = next(b)

            if c.find(a):
                rss_url = i['link']

            else:
                raise HTTPException(status_code=404, detail="Notfound Link Please recheck URL")

    News = feed(rss_url)
    return JSONResponse(News)
#-------------------Api 실행 부분-------------------

if __name__ == '__main__':
    uvicorn.run(app)