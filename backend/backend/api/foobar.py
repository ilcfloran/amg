from backend.foobar import foobar
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class FoobarRequest(BaseModel):
    number: int


class FoobarResponse(BaseModel):
    result: str


@router.post("/foobar/", response_model=FoobarResponse)
def get_consumption(request: FoobarRequest):
    return FoobarResponse(result=foobar(request.number))
