from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

# 뉴스 내용 전체 삭제
@router.delete('/all', tags=["news"])
async def news_data_del_all():
    result = pre_request.pre_del_all()

    return result
