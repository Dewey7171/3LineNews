import uvicorn
from fastapi import FastAPI
from sqlalchemy import *
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sql_auth
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
sql = sql_auth.app

engine = create_engine(
    sql['name'] + '://' + sql['user']+ ':'+sql['password']+'@'+sql['host']+'/'+sql['db'])

conn = engine.connect()
metadata = db.MetaData()

Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get('/a')
async def sql():
    table = db.Table('newdata', metadata, autoload=True, autoload_with=engine)
    a = session.query(table).all()
    return a

@app.get('/b')
async def sql():
    table1 = db.Table('news_link', metadata, autoload=True, autoload_with=engine)
    b = session.query(table1).all()
    return b

if __name__ == '__main__':
    uvicorn.run(app)


# query = db.select([table])
# result = conn.execute(query)
# result_set = result.fetchall()
