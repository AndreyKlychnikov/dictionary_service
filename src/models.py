from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PartOfSpeech(Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PRONOUN = "pronoun"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    NUMERAL = "numeral"
    ARTICLE = "article"
    DETERMINER = "determiner"


# @dataclass
class Definition(BaseModel):
    text: str
    example: Optional[str]


# @dataclass
class Word(BaseModel):
    part_of_speech: PartOfSpeech
    audio_url: str
    definitions: List[Definition]
