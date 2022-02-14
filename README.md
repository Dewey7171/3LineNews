# 뉴스 3줄 요약 API

Fastapi를 이용해 뉴스를 3줄 요약해 json형태의 데이터로 출력하는 api

1. 자신이 원하는 뉴스 사이트의 최신 기사들을 제목, 링크, 3줄 요약 데이터를 JSON형식으로 받는다.


2. Mysql DB에 요약된 기사 데이터를 저장 시킨다.


3. DB에 저장된 데이터를 유저들이 호출한다.

</br></br>

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
<img src="https://img.shields.io/badge/Python-3766AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white">


</br></br></br>

# 사용방법 
기본 IP = 0.0.0.0</br>
기본 PORT = 0000
</br></br>

### GET 0.0.0.0:0000/news/all
  👉DB에 저장된 뉴스 내용 전체 호출</br>
      __ex: 0.0.0.0:0000/news/all  -> 저장된 전체 데이터 호출__
  </br>
  </br>
### GET 0.0.0.0:0000/news/newslist
  👉DB에 저장된 News_link Table 호출</br>
      __ex: 0.0.0.0:0000/newslist  -> 뉴스 리스트 호출__
  </br>
  </br>
### GET 0.0.0.0:0000/news/site/{newsname}
  👉newdata Table에 존재하는 newsname인 데이터를 호출</br>
      __ex: 0.0.0.0:0000/news/inven  -> inven이라는 이름을 가진 뉴스 데이터 호출__
  </br>
  </br>
### GET 0.0.0.0:0000/news/date/{date}
  👉newdata Table에 존재하는 date 해당 날짜의 기사 데이터를 호출 </br>
      __ex: 0.0.0.0:0000/date/2021-09-30  -> 2021년 9월 30일 날짜의 뉴스 데이터를 호출__
</br></br></br>

# DB 스키마

### news_link
~~~
create table news_link
(
	id int auto_increment comment
		primary key,
    
	name varchar(50) not null,
  
	link varchar(500) not null comment ,
  
	constraint news_link_link_uindex
		unique (link),
    
	constraint news_link_name_uindex
		unique (name)
);


id = 저장되는 뉴스 링크를 구별할 수 있는 id
name = 뉴스 이름을 나타내는 column, unique로 고유한 이름을 가지도록 만듬, 중복 x
link = 뉴스 링크를 나타내는 column, unique로 고유한 링크를 가지도록 만듬, 중복 x

~~~
</br></br>
### news_data

~~~
create table news_data
(
	id bigint auto_increment
		primary key,
    
	data json not null,
  
	name varchar(30) not null,
  
	newsurl varchar(500) not null,
  
	constraint newdata_newsurl_uindex
		unique (newsurl)
);

id = 저장되는 데이터를 구별할 수 있는 id
data = 뉴스 데이터를 JSON형식으로 저장하는 column, date,title,content로 구성되어있음
name = 어떤 뉴스인지 구별하기 위한 column
newsurl = url을 저장하는 column, 데이터 중복을 막기위한 조치로 고유한 데이터인 url을 unique시켜 중복을 막음

~~~


## 이후 진행할 사항

1. 구독 기능 만들기 & 자동 발송 기능
2. DB 변경 및 리팩토링
3. TDD 적용 해보기
