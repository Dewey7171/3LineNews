from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connection_db import sql_auth

sql = sql_auth.app

class engineconn:

    def __init__(self):
        self.engine = create_engine(sql['name'] + '://' + sql['user'] + ':' + sql['password'] + '@'+ sql['host'] + ':' + sql['port'] + '/' + sql['db'], pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn