from feed_parser import feed
from sqlalchemy import *
from connection_db import db_connection, db_class as db

#------------------Mysql 설정 부분------------------
engine = db_connection.engineconn()
metadata = MetaData()
session = engine.sessionmaker()

table = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)
news = session.query(table).all()


#------------------Mysql 설정 부분------------------

for i in news:
    news_links = i['link']
    news_name = i['name']
    news_source = feed(news_links)

    for data in news_source:
        newsurl = data["url"]
        del data["url"]
        add_data = db.Newsdata(data=data, name=news_name, newsurl=newsurl)
        session.add(add_data)
        try:
            session.commit()
        except:
            print('데이터 중복')
            pass

session.close()
session.execute("set @count = 0")
session.commit()
session.execute("update newdata set id = @count:=@count+1;")
session.commit()
session.close()


