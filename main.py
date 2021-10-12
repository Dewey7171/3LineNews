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
        news_url = "SELECT url FROM newdata"
        develop_cursor.execute(news_url)
        check_url = develop_cursor.fetchall()


        dataUpdates = " INSERT INTO newdata VALUES(default,%s,%s,%s,%s,default,%s)"
        NewsData = News[data]
        for url_check in check_url:
            if url_check['url'] == NewsData['url']:
                # HTTPException(status_code=403, detail="Duplicate Data")
                print('중복 데이터 존재')
                pass
            elif url_check['url'] != NewsData['url']:
                datasaver = []
                datasaver.append(NewsData['title'])
                datasaver.append(NewsData['content'])
                datasaver.append(NewsData['url'])
                datasaver.append(news_name)
                datasaver.append(NewsData['date'])
                develop_cursor.execute(dataUpdates, datasaver)
            else:
                print('데이터가 존재 하지 않습니다.')

connect_cursor.conn_commit()
connect_cursor.conn_close()

#------------------Class 선언 부분------------------
# class addNews(BaseModel):
#     name : Optional[str]
#     link : Optional[str]
#------------------Class 선언 부분------------------

#
# #-------------------Api 실행 부분-------------------
# @app.get("/news_list")
# async def Newslist():
#
#     develop_cursor.execute(news_link_search)
#     newslist = develop_cursor.fetchall()
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#
#     return newslist
#
#
# # db에 새로운 링크 집어 넣는 곳
# @app.post("/addnews")
# async def UpdateNews(addnews : addNews):
#
#     new_News = []
#     # 근데 여기에 rss 링크가 아닌 일반 링크가 들어오면 망치는데 어떡하지?
#     # 이 작업은 어디서 해야될까? feed_parser에서 진행해야 될 것으로 보이긴함
#
#     updates =" INSERT INTO news_link VALUES(default,%s,%s)"
#     add_new_Data = dict(addnews)
#
#     new_News.append(add_new_Data['name'])
#     new_News.append(add_new_Data['link'])
#
#     develop_cursor.execute(updates,new_News)
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#
#     return HTTPException(status_code=200, detail="SUCCESS INSERT DATA")

# @app.get("/news/{news_name}")
# async def News(news_name: str):
#
#     # 뉴스 리스트 속에 있는 뉴스들을 찾아서 rss_url로 저장하는 구문
#     for i in news_link_result:
#         newsNameData = i['name']
#         if news_name.lower() == newsNameData:
#             b = iter(i)
#             c = next(b)
#             if c.find(newsNameData):
#                 rss_url = i['link']
#             else:
#                 raise HTTPException(status_code=404, detail="Notfound Link Please recheck URL")
#
#     News = feed(rss_url)
#
#
#     newdata_search = "SELECT * FROM newdata"
#     develop_cursor.execute(newdata_search)
#
#     # 현재 이 반복문은 News 리스트 속 존재하는 딕셔너리를 추출하는 구문
#     # 추출한 딕셔너리를 datasaver라는 리스트에 하나씩 집어넣어 DB 컬럼에 맞게 집어 넣는다.
#     # 현재 DB의 모든 Column은 NOT NULL이 적용되어 있는데 만약 NULL값이 들어오면 오류가 발생함
#     # 이러한 NULL값에 대한 방지로 Not null 해제 해놓고 이에 대한 추가 수정 필요
#     for data in range(0,len(News)):
#         datasaver = []
#         dataUpdates = " INSERT INTO newdata VALUES(default,%s,%s,%s,%s,default,%s)"
#         NewsData = News[data]
#
#         datasaver.append(NewsData['title'])
#         datasaver.append(NewsData['content'])
#         datasaver.append(NewsData['url'])
#         datasaver.append(news_name)
#         datasaver.append(NewsData['date'])
#
#         develop_cursor.execute(dataUpdates, datasaver)
#
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#     return datasaver

# @app.get("/")
# async def main():
#     main = "fastapi 메인"
#     return main
#
#
# #-------------------Api 실행 부분-------------------
#
# if __name__ == '__main__':
#     uvicorn.run(app)

