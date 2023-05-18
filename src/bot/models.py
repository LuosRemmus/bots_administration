from typing import Optional
from pydantic import BaseModel

class BaseBotModel(BaseModel):
    id: int

class PostBotModel(BaseModel):
    alias: str
    description: str
    token: str
    name: str

class PostRespBotModel(BaseBotModel):
    pass

class GetBotModel(BaseBotModel):
    name: str
    alias: str
    description: Optional[str]
    token: str

    class Config:
        orm_mode = True

class PutBotModel(PostBotModel):
    alias: Optional[str]
    description: Optional[str]
    token: Optional[str]
    name: Optional[str]

