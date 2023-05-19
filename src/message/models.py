from typing import Optional
from pydantic import BaseModel

class MessageModel(BaseModel):
    channel_id: Optional[int]
    message: Optional[str]
