
import sql_auth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sql = sql_auth.app



class engine:

    def __init__(self):
        self.engine = create_engine(sql['name'] + '://' + sql['user']+ ':'+sql['password']+'@'+sql['host']+':'+sql['port']+'/'+sql['db'], pool_recycle =500)


    def session(self):
        # scoped_session은 사용할 것인가 말 것인가?
        # main호출에서는 비동기 작업이 이루어지지 않음
        # API호출에서는 비동기 작업이 이루어짐
        Session = sessionmaker(autocommit=False,autoflush=False,bind=self.engine)

        return Session
    def connection(self):
        conn = self.engine.connect()

        return conn