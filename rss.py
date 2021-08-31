import feedparser
from newspaper import Article


from typing import List
from textrankr import TextRank

#게임 동아 "https://game.donga.com/feeds/rss"
#인벤 "http://feeds.feedburner.com/inven"
#게임 인사이트 "http://feeds.feedburner.com/inven"
#루리웹 "https://bbs.ruliweb.com/news/rss"
#더게임스데일리 "http://www.tgdaily.co.kr/rss/allArticle.xml"

#---------------뉴스 사이트---------------
rss_url = "http://feeds.feedburner.com/inven"
#
rss_feed = feedparser.parse(rss_url)

news_list = []
news_data = {
    "title" : "",
    "content" : "",
    "url" : ""
}

# rss feed에는 총 25개의 뉴스 기사만 보여진다.
#----------------------------------------


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

#----------------------------------------------------------



#------------------ 뉴스 요약 데이터 ---------------------
def a ():
    for feed in rss_feed.entries[:5]:
        #  rss_feed 속 뉴스 링크 분류

        #article에 링크 속 뉴스 본문 가져와 저장한다.
        article = Article(feed.link, language = 'ko')
        article.download()
        article.parse()

        NewsTitle = article.title
        NewsFeed = article.text
        NewsUrl = article.url
        NewsTime = article.publish_date

    # 뉴스 본문들을 요약하고 k줄 만큼 요약해 str형식으로 저장한다
        summarized: str = textrank.summarize(NewsFeed, k)

        news_data["title"] = NewsTitle
        news_data["content"] = summarized
        news_data["url"] = "<A href=\""+NewsUrl+"\" target = \"blank\">"+NewsUrl +"</A>"+"<br>"

        news_content = news_data.copy()
        news_list.append(news_content)



a = news_list[0]['title']

print(type(a))
#-------------- 뉴스 요약 본 정렬 구문----------------
# MIMEText html로 보내는 것
#AST Abstract Syntax Tree 얘를 이용해서 만들어보기


news_list1 = str(news_list)


news_list_title = news_list1.replace("'title':", "<br><br>")
news_list_content = news_list_title.replace("'content':", "<br><br>")
news_list_url = news_list_content.replace("'url':", "<br><br>")



