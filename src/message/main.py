from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("/")
def send_message(message: str):
    try:
        pass
    except:
        pass
