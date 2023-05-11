from fastapi import FastAPI

app = FastAPI()


@app.post("/channels/")
def bind(channel: str):
    try:
        pass
    except:
        pass


@app.delete("/channels/{channel_id}")
def delete_channel(channel_id: int):
    try:
        pass
    except:
        pass


@app.post("/channels/")
def direct_bind(bot_id: int):
    try:
        pass
    except:
        pass


@app.get("/channels/{channel_id}")
def channel_info(channel_id: int):
    try:
        pass
    except:
        pass


@app.get("/channels/")
def get_channels():
    try:
        pass
    except:
        pass