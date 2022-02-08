import json
import redis

from test_feed import feed
from datetime import date
# 휘발성이니까 데이터가 날라감


rd = redis.StrictRedis(host='localhost', port=6379, db=0)

data = feed("http://feeds.feedburner.com/inven")
date_time = str(date.today())

jsonDataDict = json.dumps(data, ensure_ascii=False).encode('utf-8')

rd.set(date_time,jsonDataDict)



# 레디스를 쓰는 이유가 뭔지 생각해보기
#

