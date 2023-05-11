from fastapi import APIRouter

router = APIRouter(
    prefix="/channels",
    tags=["Channels"]
)


@router.post("/")
def bind(channel: str):
    try:
        pass
    except:
        pass


@router.delete("/{channel_id}")
def delete_channel(channel_id: int):
    try:
        pass
    except:
        pass


@router.post("/")
def direct_bind(bot_id: int):
    try:
        pass
    except:
        pass


@router.get("/{channel_id}")
def channel_info(channel_id: int):
    try:
        pass
    except:
        pass


@router.get("/")
def get_channels():
    try:
        pass
    except:
        pass