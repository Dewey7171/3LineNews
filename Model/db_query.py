from sqlalchemy import Table
from Model import db_connection
from Model import db_class

engine = db_connection.engineconn()
session = engine.sessionmaker()
newsdata = db_class.Newsdata
newslink = db_class.Newslink

def db_commit():

    return session.commit()

def db_close():

    return session.close()

def db_newsdata_get():
    result = session.query(newsdata).all()

    return result

def db_newslist_get():
    result = session.query(newslink).all()

    return result

def db_newslink_post(addlist):
    add = newslink(name=addlist.name,link=addlist.link)
    result = session.add(add)

    return result

def db_newsdata_get_news(news):
    result = session.query(newsdata).filter(newsdata.name == news).all()

    return result

def db_newsdata_get_date(date):
    result = session.query(newsdata).filter(newsdata.data.comparator['date'] == date).all()

    return result

def db_newsdata_del_all():
    result = session.query(newsdata).delete()

    return result

