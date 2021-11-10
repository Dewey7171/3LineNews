from feed_parser import feed
import sql_auth
import sqlalchemy as db
from itertools import chain
import dbconn


#------------------Mysql 설정 부분------------------
sql = sql_auth.app

engine = dbconn.engine
metadata = db.MetaData()
connection = engine.connection()

Session = engine.session()




table = db.Table('news_link', metadata, autoload=True, autoload_with=engine)
news_data = db.Table('newdata', metadata, autoload=True, autoload_with=engine)
news = Session.query(table).all()

links_list = []

#------------------Mysql 설정 부분------------------

# 데이터 넣는 부분을 최적화 시키는 코드를 고민해서 작성해보기
for i in news:
    news_links = i['link']
    news_name = i['name']
    News = feed(news_links)

    for data in range(0, len(News)):
        NewsData = News[data]
        datasaver = list(chain(NewsData['title'],NewsData['content'],NewsData['url'],news_name,NewsData['date']))
        dataUpdates = db.insert(news_data)

        try:
            connection.execute(dataUpdates, datasaver)
        except:
            print('URL Duplicate Reload Data')
            pass
Session.commit()


# query = db.insert(table)
# values_list = [{'id': 'dork', 'passwd': '1234'}, {'id': 'test', 'passwd':'test123', 'email':'test@test.com'}]
# result_proxy = connection.execute(query, values_list)
# result_proxy.close()


