import feedparser
from newspaper import Article
from textrankr import TextRank
from typing import List



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

def feed(rss_url : str) :

    rss_feed = feedparser.parse(rss_url)

    news_list = []
    news_data = {
        "title": "",
        "content": "",
        "url": ""
    }

    for feed in rss_feed.entries[:3]:
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

    return news_list