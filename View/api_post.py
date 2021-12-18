from pydantic import BaseModel
from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

class Addnews(BaseModel):
    name: str
    link: str

@router.post('/newslist', tags=["news"])
async def news_list_post_add(add : Addnews):
    result = pre_request.pre_post_list(add)

    return result