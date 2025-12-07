from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id : int
    name : str
    desc : Optional[str] = None