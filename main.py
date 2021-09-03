import json
from enum import Enum
import logging

import feedparser

from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from newspaper import Article
from typing import List, Optional

from passlib.context import CryptContext
from jose import JWTError, jwt

from pydantic import BaseModel
from starlette.responses import JSONResponse
from textrankr import TextRank
from fastapi import FastAPI, Depends, HTTPException, status

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "123", "owner": current_user.username}]






#리스트형식으로 저장하기 위한 클래스 선언
class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens

# 리스트 형식으로 저장하는 공간을 만들고 그 공간에 데이터들을 요약한다.
mytokenizer: MyTokenizer = MyTokenizer()
textrank: TextRank = TextRank(mytokenizer)
# 요약한 데이터는 3줄까지 가능하도록 설정하는 변수
k: int = 3

#-------------------------------------------------------------
class NewsName(str, Enum):
    inven = "inven"
    ruliweb = "ruliweb"
    gameinsight = "gameinsight"

@app.get("/{news_name}")
async def get_model(news_name: NewsName):

    if news_name == NewsName.inven:
        rss_url = "http://feeds.feedburner.com/inven"
        rss_feed = feedparser.parse(rss_url)
        news_list = []
        news_data = {
            "title": "",
            "content": "",
            "url": ""
        }

        for feed in rss_feed.entries[:2]:
            #  rss_feed 속 뉴스 링크 분류

            # article에 링크 속 뉴스 본문 가져와 저장한다.
            article = Article(feed.link, language='ko')
            article.download()
            article.parse()

            NewsTitle = article.title
            NewsFeed = article.text
            NewsUrl = article.url

            # 뉴스 본문들을 요약하고 k줄 만큼 요약해 str형식으로 저장한다
            summarized: str = textrank.summarize(NewsFeed, k)

            news_data["title"] = NewsTitle
            news_data["content"] = summarized
            news_data["url"] = NewsUrl

            news_content = news_data.copy()
            news_list.append(news_content)
        return JSONResponse(news_list), logging.info("ifo로그입니다.")



    if news_name.value == "ruliweb":

        rss_url = "https://bbs.ruliweb.com/news/rss"
        rss_feed = feedparser.parse(rss_url)
        news_list = []
        news_data = {
            "title": "",
            "content": "",
            "url": ""
        }

        for feed in rss_feed.entries:
            #  rss_feed 속 뉴스 링크 분류

            # article에 링크 속 뉴스 본문 가져와 저장한다.
            article = Article(feed.link, language='ko')
            article.download()
            article.parse()

            NewsTitle = article.title
            NewsFeed = article.text
            NewsUrl = article.url

            # 뉴스 본문들을 요약하고 k줄 만큼 요약해 str형식으로 저장한다
            summarized: str = textrank.summarize(NewsFeed, k)

            news_data["title"] = NewsTitle
            news_data["content"] = summarized
            news_data["url"] = NewsUrl

            news_content = news_data.copy()
            news_list.append(news_content)
        return JSONResponse(news_list)

    if news_name.value == "gameinsight":

        rss_url = "http://www.gameinsight.co.kr/rss/allArticle.xml"
        rss_feed = feedparser.parse(rss_url)
        news_list = []
        news_data = {
            "title": "",
            "content": "",
            "url": ""
        }

        for feed in rss_feed.entries:
            #  rss_feed 속 뉴스 링크 분류

            # article에 링크 속 뉴스 본문 가져와 저장한다.
            article = Article(feed.link, language='ko')
            article.download()
            article.parse()

            NewsTitle = article.title
            NewsFeed = article.text
            NewsUrl = article.url

            # 뉴스 본문들을 요약하고 k줄 만큼 요약해 str형식으로 저장한다
            summarized: str = textrank.summarize(NewsFeed, k)

            news_data["title"] = NewsTitle
            news_data["content"] = summarized
            news_data["url"] = NewsUrl

            news_content = news_data.copy()
            news_list.append(news_content)
        return JSONResponse(news_list)

#----------------------------------------------------------

