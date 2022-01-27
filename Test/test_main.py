from datetime import date
from fastapi import FastAPI
from Presenter.pre_feed_parser import feed

import json
import redis



app = FastAPI()

rd = redis.StrictRedis(host='localhost', port=6379, db=0)


# 뉴스 내용 전체 호출
@app.get('/all', tags=["news"])
async def get_all():
    data = rd.get('q')
    result = json.loads(data)


    return result