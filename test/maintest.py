from add_package.feed_parser import feed
from connection_db import sql_auth


sql = sql_auth.app
dbconn = db.dbconn
#------------------Mysql 설정 부분------------------

connect_cursor = dbconn('News')
develop_cursor = connect_cursor.conn_cursor()

# news
news_link_search = "SELECT * FROM news_link"
develop_cursor.execute(news_link_search)
news_link_result = develop_cursor.fetchall()

links_list = []

# ------------------Mysql 설정 부분------------------
for i in news_link_result:
    news_links = i['link']
    news_name = i['name']
News = feed('https://www.inven.co.kr/webzine/news/rss.php')
news_name = '인벤'
for data in range(0, len(News)):

    dataUpdates = "INSERT INTO newdata VALUES(default,%s,%s,%s,%s,%s)"
    NewsData = News[data]
    datasaver = []
    datasaver.append(NewsData['title'])
    datasaver.append(NewsData['content'])
    datasaver.append(NewsData['url'])
    datasaver.append(news_name)
    datasaver.append(NewsData['date'])
    print(datasaver)

    try:
        develop_cursor.execute(dataUpdates, datasaver)
    except:
        print('URL Duplicate Reload Data')
        Sortid = "set @count = 0"
        develop_cursor.execute(Sortid)
        connect_cursor.conn_commit()
        idSort = "update newdata set id = @count:=@count+1;"
        develop_cursor.execute(idSort)
        connect_cursor.conn_commit()
        pass

connect_cursor.conn_commit()
connect_cursor.conn_close()
