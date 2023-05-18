from typing import Optional
from pydantic import BaseModel


class PostMessageModel(BaseModel):
    channel_id: Optional[int]
    message: Optional[str]
