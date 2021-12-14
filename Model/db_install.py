from Model import db_class
from Model import db_connection

enginconn = db_connection.engineconn()

def table_install():
    db_class.Newsdata.__table__.create(bind=enginconn.engine, checkfirst=True)
    db_class.Newslink.__table__.create(bind=enginconn.engine, checkfirst=True)