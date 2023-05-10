from fastapi import FastAPI

app = FastAPI()


@app.post("/bots/")
def add_bot(alias: str, description: str, token: str, name: str):
    try:
        return {
            "status": 200,
            "data": {
                "id": "id",
                "new": True
            }
        }
    except Exception as ex:
        print(ex)
        return {
            "status": 503,
            "message": "Бот уже есть в базе"
        }


@app.delete("/bots/{bot_id}")
def delete_bot(bot_id: int):
    try:
        return {
            "status": 200,
            "data": {
                "id": bot_id,
                "message": "deleted"
            }
        }
    except Exception as ex:
        print(ex)
        return {
            "status": 503,
            "message": "Бот отсутствует в базе"
        }


@app.patch("/bots/{bot_id}")
def update_bot(bot_id: int):
    try:
        pass
    except Exception as ex:
        print(ex)


@app.get("/bots/{bot_id}")
def get_bot_info(bot_id: int):
    try:
        pass
    except Exception as ex:
        print(ex)


@app.get("/bots/")
def get_bots():
    try:
        pass
    except:
        print()


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


@app.post("/messages/")
def send_message(message: str):
    try:
        pass
    except:
        pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        pass
    except:
        pass
