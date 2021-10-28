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

# news
news_link_search = "SELECT * FROM news_link"
develop_cursor.execute(news_link_search)
news_link_result = develop_cursor.fetchall()

links_list = []

# a = "ALTER TABLE newdata AUTO_INCREMENT=1"
# develop_cursor.execute(a)
# connect_cursor.conn_commit()
# connect_cursor.conn_close()
#------------------Mysql 설정 부분------------------


for i in news_link_result:
    news_links = i['link']
    news_name = i['name']
    News = feed(news_links)
    # 현재 이 반복문은 News 리스트 속 존재하는 딕셔너리를 추출하는 구문
    # 추출한 딕셔너리를 datasaver라는 리스트에 하나씩 집어넣어 DB 컬럼에 맞게 집어 넣는다.
    # 현재 DB의 모든 Column은 NOT NULL이 적용되어 있는데 만약 NULL값이 들어오면 오류가 발생함
    # 이러한 NULL값에 대한 방지로 Not null 해제 해놓고 이에 대한 추가 수정 필요


    for data in range(0, len(News)):
        # news_url = "SELECT url FROM newdata"
        # develop_cursor.execute(news_url)
        # check_url = develop_cursor.fetchall()

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
