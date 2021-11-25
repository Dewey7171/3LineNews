
from sqlalchemy import Column, BigInteger, VARCHAR, JSON, TEXT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Newdata(Base):
    __tablename__ = 'newdata'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    content = Column(JSON,nullable=False)
    name = Column(VARCHAR(30),nullable=False)

class Newslink(Base):
    __tablename__ = 'news_link'
    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    link = Column(TEXT, nullable=False)