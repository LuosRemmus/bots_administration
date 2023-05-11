from fastapi import FastAPI

app = FastAPI()


@app.post("/messages/")
def send_message(message: str):
    try:
        pass
    except:
        pass