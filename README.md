# 뉴스 3줄 요약 API

Fastapi를 이용해 뉴스를 3줄 요약해 json형태의 데이터로 출력하는 api

1. 자신이 원하는 뉴스 사이트의 최신 기사들을 제목, 링크, 3줄 요약 데이터를 JSON형식으로 받는다.


2. Mysql DB에 요약된 기사 데이터를 저장 시킨다.


3. DB에 저장된 데이터를 유저들이 호출한다.
=======
# ✋뉴스 3줄 요약 API

📰뉴스 기사를 3줄로 요약해서 유저들에게 제공하는 RESTAPI 서비스

</br>
</br>
</br>

## Fastapi를 이용해 뉴스를 3줄 요약해 json형태의 데이터로 출력하는 api

> 1. 자신이 원하는 뉴스 사이트의 최신 기사들을 제목, 링크, 3줄 요약 데이터를 JSON형식으로 받는다.
> 
>  2. Mysql DB에 요약된 기사 데이터를 저장 시킨다.
>  
>  3. DB에 저장된 데이터를 유저들이 호출한다.
</br>
</br>
</br>

# 실행환경 / 주요기술
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> <img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=aws&logoColor=white"> <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=aws&logoColor=white">
</br> </br>
<img src="https://img.shields.io/badge/Python-3766AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white">


  
</br>
</br>
</br>

# 사용방법 
기본 IP = 13.209.99.213</br>
기본 PORT = 22555
</br>
</br>
### GET 13.209.99.213/newslist
  👉DB에 저장된 News_link Table 호출</br>
      __ex: 13.209.99.213:22555/newslist  -> 해당 테이블 속 전체 데이터 호출__
  </br>
  </br>
### GET 13.209.99.213/news/{newsname}
  👉newdata Table에 존재하는 newsname인 데이터를 호출</br>
      __ex: 13.209.99.213:22555/news/inven  -> inven이라는 이름을 가진 뉴스 데이터 호출__
  </br>
  </br>
### GET 13.209.99.213/date/{date}
  👉newdata Table에 존재하는 date 해당 날짜의 기사 데이터를 호출 </br>
      __ex: 13.209.99.213:22555/date/2021-09-30  -> 2021년 9월 30일 날짜의 뉴스 데이터를 호출__


### DB 정보와 같은 보안에 관련된 사항은 언제나 ignore 해 놓기 