import pymysql
import uvicorn
import sql_auth

from starlette.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from feed_parser import feed
# to get a string like this run:
# openssl rand -hex 32

app = FastAPI()

sql = sql_auth.app

conn = pymysql.Connect(
    db=sql['db'],
    host=sql['host'],
    user=sql['user'],
    password=sql['password'],
    charset=sql['charset'])

s = conn.cursor()


#-------------------------------------------------------------

@app.get("/{news_name}")
async def get_model(news_name: str):

#if는 한 번에

    if news_name.lower() == "inven":
        rss_url = "http://feeds.feedburner.com/inven"

    elif news_name.lower() == "ruliweb":
        rss_url = "https://bbs.ruliweb.com/news/rss"

    elif news_name.lower() == "gameinsight":
        rss_url = "http://www.gameinsight.co.kr/rss/allArticle.xml"
# {
    # inven : http://feeds.feedburner.com/inven
    # inven : http://feeds.feedburner.com/inven
    # dict
    # }
    else:
        raise HTTPException(status_code=404, detail="Item not found")

    News = feed(rss_url)

    return JSONResponse(News)

#----------------------------------------------------------

if __name__ == '__main__':
    uvicorn.run(app)