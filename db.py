import pymysql
import sql_auth
from sqlalchemy import *
import sqlalchemy as db

sql = sql_auth.app

class dbconn:

    # dbconn을 호출하면 맨 처음 나오는 DB연결 기본 함수
    def __init__(self,dbname:str):
        self.connect = pymysql.Connect(
            db=dbname,
            host=sql['host'],
            user=sql['user'],
            password=sql['password'],
            charset=sql['charset'],
            port=sql['port']
            )

    # DB를 연결해 이용하기 위한 커서 연결 함수
    def conn_cursor (self):
        self.connect.ping(reconnect=True)
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


engine = create_engine(sql['name'] + '://' + sql['user']+ ':'+sql['password']+'@'+sql['host']+'/'+sql['db'])

conn = engine.connect()
metadata = db.MetaData()
table = db.Table('newdata',metadata,autoload=True, autoload_with = engine)

print(table.columns.keys())
query = db.select([table])

result = conn.execute(query)
result_set = result.fetchall()
row = result.fetchone()
print(row._mapping['title'])


