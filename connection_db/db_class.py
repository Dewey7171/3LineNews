
from sqlalchemy import Column, BigInteger, VARCHAR, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Newdata(Base):
    __tablename__ = 'newdata'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(500),nullable=False)
    content = Column(Text,nullable=False)
    url = Column(VARCHAR(255),nullable=False)
    newsname = Column(VARCHAR(50),nullable=False)
    recordtime = Column(TIMESTAMP,nullable=False)