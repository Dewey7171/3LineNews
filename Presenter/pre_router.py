from View import RestAPI
from fastapi import APIRouter

api_router = APIRouter
api_router.include_router(RestAPI.router, tags=["news"])