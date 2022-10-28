from fastapi import APIRouter
from backend.api import foobar

api_router = APIRouter()
api_router.include_router(foobar.router)
