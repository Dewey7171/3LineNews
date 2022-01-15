import json
import redis

from test_feed import feed
from datetime import date
# 휘발성이니까 데이터가 날라감


rd = redis.StrictRedis(host='localhost', port=6379, db=0)

data = feed("http://feeds.feedburner.com/inven")
a = str(date.today())
b = 'q'
jsonDataDict = json.dumps(data, ensure_ascii=False).encode('utf-8')
#
rd.set(b,jsonDataDict)
asd = rd.get('q')
qwert = json.loads(asd)

print(qwert[0]['summary'])

