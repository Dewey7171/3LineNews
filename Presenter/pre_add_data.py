from pre_feed_parser import feed
from sqlalchemy import *
from Model import db_connection, db_class as db

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

# 이 부분도 if로 가르면 안되나?
# 해당하는 부분은 성능에 치명적일 수 있으니 이 부분을 생각해서 어떻게 처리를 하면 좋을지 생각해보자.
# id를 보여주지 말까 그냥?
# session.execute("set @count = 0")
# session.commit()
# session.execute("update newdata set id = @count:=@count+1;")
# session.commit()
# session.close()


