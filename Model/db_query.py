from Model import db_connection
from Model import db_class

engine = db_connection.engineconn()
session = engine.sessionmaker()
newsdata = db_class.Newsdata
newslink = db_class.Newslink

# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

# NEWSDATA GET
def db_newsdata_get():
    result = session.query(newsdata).all()

    return result

# NEWSLIST GET
def db_newslist_get():
    result = session.query(newslink).all()

    return result

# NEWSDATA NAME GET
def db_newsdata_get_news(news):
    result = session.query(newsdata).filter(newsdata.name == news).all()

    return result

# NEWSDATA DATE GET
def db_newsdata_get_date(date):
    result = session.query(newsdata).filter(newsdata.data.comparator['date'] == date).all()

    return result

# NEWSLINK ADD
def db_newslink_post(addlist):
    add = newslink(name=addlist.name,link=addlist.link)
    result = session.add(add)

    return result

# NEWSLINK DELETE
def db_newsdata_del_all():
    result = session.query(newsdata).delete()

    return result

# NEWSLINK UPDATE
def db_newslist_patch(patchlist, id):
    result = session.query(newslink).filter(newslink.id == id).update({'name':patchlist.name,'link':patchlist.link})

    return result

def db_subscribe_email(email):
    # add = userdata(email=email)
    result = session.add()

    return result

