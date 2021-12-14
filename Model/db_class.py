from sqlalchemy import Column, BigInteger, VARCHAR, JSON, TEXT,Computed
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 가상 컬럼은 Computed로 불러와서 쓸 수 있다는데 공식 문서를 봐도 이해가 안감
# 이 부분도 적용 시킨다면 훨씬 더 효과적으로 DB를 제어할 수 있을 듯 싶다.

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
