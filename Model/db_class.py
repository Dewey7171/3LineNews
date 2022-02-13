from sqlalchemy import Column, BigInteger, VARCHAR, JSON, TEXT,INT,BOOLEAN
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Newsdata(Base):
    __tablename__ = 'news_data'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    data = Column(JSON ,nullable=False)
    name = Column(VARCHAR(30), nullable=False)
    newsurl = Column(VARCHAR(500), nullable=False, unique=True)

class Newslink(Base):
    __tablename__ = 'news_link'
    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    link = Column(TEXT, nullable=False)

class Subcribe(Base):
    __tablename__ = 'subscribe_data'
    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(60), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    active = Column(BOOLEAN,default=0)
    keys = Column(INT, nullable=False)