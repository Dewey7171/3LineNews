from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

# 뉴스 내용 전체 호출
@router.get('/all', tags=["news"])
async def news_data_get_all():
    result = pre_request.pre_get_all()

    return result

# 뉴스 사이트 전체 호출
@router.get('/newslist', tags=["news"])
async def news_list_get_all():
    result = pre_request.pre_get_list()

    return result

# 뉴스 사이트 별 조회
@router.get('/site/{news}', tags=["news"])
async def news_name_get(news : str):
    result = pre_request.pre_get_newsdata(news)

    return result
# 뉴스 날짜별 조회
@router.get('/date/{date}', tags=["news"])
async def news_date_get(date : str):
    result = pre_request.pre_get_date(date)

    return result

# 일단 get으로 호출 시 메세지를 보낸다
@router.get('/msg', tags=["news"])
async def news_date_get():
    result = pre_request.pre_slack_msg()

    return result