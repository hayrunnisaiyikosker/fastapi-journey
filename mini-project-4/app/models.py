from pydantic import BaseModel
from typing import Dict


class PollCreate(BaseModel):
    question: str
    options: list[str]  


class Poll(BaseModel):
    id: str
    question: str
    options: list[str]
    votes: Dict[str, int] = {}  