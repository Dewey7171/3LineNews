import json

import feedparser

from newspaper import Article
from typing import List

from pydantic import BaseModel
from textrankr import TextRank
from fastapi import FastAPI



app = FastAPI()

rss_url = "http://feeds.feedburner.com/inven"

# rss feed에는 총 25개의 뉴스 기사만 보여진다.
rss_feed = feedparser.parse(rss_url)

news_list = []
news_data = {
    "title":"",
    "content":"",
    "url":""
}

#-------------------- 한글 요약 클래스-------------------
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

def news_sm():

    for feed in rss_feed.entries[:5]:
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
    return json.dumps(news_list, ensure_ascii=False)



@app.get("/items/{item_id}")
async def read_item(item_id: int):

    if item_id == str('inven'):
        return news_sm()
    else:
        return{"item_id":item_id}
#----------------------------------------------------------





