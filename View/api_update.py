from pydantic import BaseModel
from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

class Addnews(BaseModel):
    name: str
    link: str

@router.patch('/newslist/{id}', tags=["news"])
async def news_list_patch(id : int, add : Addnews):

    result = pre_request.pre_patch_list(add,id)

    return result