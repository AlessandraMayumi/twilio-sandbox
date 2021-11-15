import uvicorn
from fastapi import FastAPI

from sandbox import send_message

app = FastAPI()


@app.post("/")
async def receive_message_from_sandbox():
    send_message()
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
