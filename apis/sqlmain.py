from add_package.feed_parser import feed
from sqlalchemy import *
from connection_db import sql_auth, db_connection, db_class as db
from fastapi import HTTPException


#------------------Mysql 설정 부분------------------
sql = sql_auth.app
engine = db_connection.engineconn()
metadata = MetaData()
connection = engine.connection()
session = engine.sessionmaker()

table = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)
news_data = Table('newdata', metadata, autoload=True, autoload_with=engine.engine)
news = session.query(table).all()


#------------------Mysql 설정 부분------------------

# 데이터 넣는 부분을 최적화 시키는 코드를 고민해서 작성해보기
for i in news:
    news_links = i['link']
    news_name = i['name']
    news_source = feed(news_links)

    for data in news_source:
        add_data = db.Newdata(content=data,name=news_name)

        try:
            session.add(add_data)

        except:
            print("데이터 추가 안됨")
            pass

session.commit()

