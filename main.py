import uvicorn
from fastapi import FastAPI, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

from db.conn import connect

app = FastAPI()


@app.post("/")
async def receive_message_from_sandbox(From: str = Form(...), To: str = Form(...), Body: str = Form(...)):
    col = connect()
    if not col.find_one(filter={'from': From}):
        col.insert_one({'from': From, 'to': To, 'msg': [Body]})
    else:
        col.update_one({'from': From}, {'$push': {'msg': Body}})

    resp = MessagingResponse()
    response_msg = resp.message()
    response_msg.body('Two-way message')

    return Response(content=str(resp), media_type="application/xml")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
