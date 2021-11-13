from feed_parser import feed
from sqlalchemy import *
import sql_auth
from dbconn import engineconn
from sqlalchemy.orm import sessionmaker

#------------------Mysql 설정 부분------------------
sql = sql_auth.app

engine = engineconn('developer')
metadata = MetaData()
connection = engine.connection()

Session = sessionmaker(bind=engine.engine)
session = Session()

table = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)
news_data = Table('newdata', metadata, autoload=True, autoload_with=engine.engine)
news = session.query(table).all()

dbquery = select([news_data])
links_list = []

# DB CLASS

#------------------Mysql 설정 부분------------------

# 데이터 넣는 부분을 최적화 시키는 코드를 고민해서 작성해보기
for i in news:
    news_links = i['link']
    news_name = i['name']
    news_source = feed(news_links)

    for data in range(0, len(news_source)):
        datasaver = []
        NewsData = news_source[data]
        datasaver.extend([NewsData['title'],NewsData['content'],NewsData['url'],news_name,NewsData['date']])
        session.add(datasaver)
        session.commit()

        try:
            session.add(datasaver)


        except:
            print('URL Duplicate Reload Data')
            pass
session.commit()





# query = db.insert(table)
# values_list = [{'id': 'dork', 'passwd': '1234'}, {'id': 'test', 'passwd':'test123', 'email':'test@test.com'}]
# result_proxy = connection.execute(query, values_list)
# result_proxy.close()


