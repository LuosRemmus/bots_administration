from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/{task_id}")
def get_task(task_id: int):
    try:
        pass
    except:
        pass
