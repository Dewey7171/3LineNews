# from textrankr import TextRank
# from typing import List
#
# import feedparser
#
# #리스트형식으로 저장하기 위한 클래스 선언
#
# class MyTokenizer:
#     def __call__(self, text: str) -> List[str]:
#         tokens: List[str] = text.split()
#         return tokens
#
# # 리스트 형식으로 저장하는 공간을 만들고 그 공간에 데이터들을 요약한다.
# mytokenizer: MyTokenizer = MyTokenizer()
# textrank: TextRank = TextRank(mytokenizer)
# # 요약한 데이터는 3줄까지 가능하도록 설정하는 변수
# k: int = 3
#
# # 데이터 가공 없이 바로 넣으면 데이터 처리 속도가 엄청나게 빠르다.
#
# def feed(rss_url : str) :
#
#     rss_feed = feedparser.parse(rss_url)
#     data = rss_feed.entries
#     return data