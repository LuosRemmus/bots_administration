from typing import Optional
from pydantic import BaseModel

class BaseChannelModel(BaseModel):
    id: int

class PostChannelModel(BaseModel):
    channel_link: Optional[str]
    bot_link: Optional[str]
    bot_id: Optional[str]

class PostRespChannelModel(BaseChannelModel):
    pass

class GetChannelModel(BaseChannelModel):
    channel_link: Optional[str]
    bot_link: Optional[str]
    bot_id: Optional[str]

    class Config:
        orm_mode = True
