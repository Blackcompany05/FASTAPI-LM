from fastapi import APIRouter
from .service import get_depression
from .scema import DepressionRequest

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return {"message":"Chanintoan"}

@router.get('/info', tags=['Depression'])
def info():
    return {"service":"depression assessment API", "version":"1.0"}