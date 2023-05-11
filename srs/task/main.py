from fastapi import FastAPI

app = FastAPI()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        pass
    except:
        pass
