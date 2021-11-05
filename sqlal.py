from sqlalchemy import *
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sql_auth
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
sql = sql_auth.app

engine = create_engine(sql['name'] + '://' + sql['user']+ ':'+sql['password']+'@'+sql['host']+'/'+sql['db'])

conn = engine.connect()
metadata = db.MetaData()
table = db.Table('news_link',metadata,autoload=True, autoload_with = engine)

Session = sessionmaker(bind=engine)
session = Session()


a = session.query(table).all()
print(a)

session.commit()
session.close()
print(table.columns.keys())

# query = db.select([table])
# result = conn.execute(query)
# result_set = result.fetchall()
