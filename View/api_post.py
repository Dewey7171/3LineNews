from pydantic import BaseModel,EmailStr
from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

class Addnews(BaseModel):
    name: str
    link: str

class EmailData(BaseModel):
    name : str
    email : EmailStr

@router.post('/newslist', tags=["news"])
async def news_list_post_add(add : Addnews):
    result = pre_request.pre_post_list(add)

    return result


@router.post('/subscribe', tags=["subscribe"])
async def news_list_post_add(emaildata : EmailData):
    result = pre_request.pre_post_subscribe(emaildata)

    return result