from View import api_get,api_post,api_delete
from fastapi import APIRouter

api_router = APIRouter
api_router.include_router(api_get.router, tags=["get"])
api_router.include_router(api_post.router, tags=["post"])
api_router.include_router(api_delete.router, tags=["delete"])