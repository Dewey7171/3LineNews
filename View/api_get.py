from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

# 뉴스 내용 전체 호출
@router.get('/all', tags=["news"])
async def newsdata():
    result = pre_request.pre_get_all()

    return result

# 뉴스 사이트 전체 호출
@router.get('/newslist', tags=["news"])
async def news_list():
    result = pre_request.pre_get_list()

    return result

# 뉴스 사이트 별 조회
@router.get('/site/{news}', tags=["news"])
async def news_name(news : str):
    result = pre_request.pre_get_newsdata(news)

    return result

# 뉴스 날짜별 조회
@router.get('/date/{date}', tags=["news"])
async def date(date : str):
    result = pre_request.pre_get_date(date)

    return result
