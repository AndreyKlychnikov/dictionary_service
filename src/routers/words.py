from typing import List

from fastapi import APIRouter
from dependencies import get_word_info
from models import Word


router = APIRouter(
    prefix="/words",
    tags=["words"],
    responses={404: {"description": "Word not found"}},
)


@router.get("/{word}", response_model=List[Word])
async def read_word(word: str):
    word_info = await get_word_info(word)
    return word_info
