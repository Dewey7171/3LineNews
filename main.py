from fastapi import FastAPI
from feed_parser import feed

import pymysql
import sql_auth

app = FastAPI()
sql = sql_auth.app

#------------------Mysql 설정 부분------------------
class dbconn:

    # dbconn을 호출하면 맨 처음 나오는 DB연결 기본 함수
    def __init__(self,dbname:str):
        self.connect = pymysql.Connect(
            db=dbname,
            host=sql['host'],
            user=sql['user'],
            password=sql['password'],
            charset=sql['charset']
            # port=55222
            )

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

news_link_search = "SELECT * FROM news_link"
develop_cursor.execute(news_link_search)
news_link_result = develop_cursor.fetchall()

links_list = []

#------------------Mysql 설정 부분------------------


for i in news_link_result:
    news_links = i['link']
    news_name = i['name']
    News = feed(news_links)

    for data in range(0, len(News)):

        dataUpdates = " INSERT INTO newdata VALUES(default,%s,%s,%s,%s,%s)"
        NewsData = News[data]
        datasaver = []
        datasaver.append(NewsData['title'])
        datasaver.append(NewsData['content'])
        datasaver.append(NewsData['url'])
        datasaver.append(news_name)
        datasaver.append(NewsData['date'])
        try:
            develop_cursor.execute(dataUpdates, datasaver)
        except:
            print('URL Duplicate Reload Data')
            pass
        finally:
            Sortid = "set @count = 0"
            develop_cursor.execute(Sortid)
            connect_cursor.conn_commit()
            idSort = "update newdata set id = @count:=@count+1;"
            develop_cursor.execute(idSort)
            connect_cursor.conn_commit()

connect_cursor.conn_commit()
connect_cursor.conn_close()
