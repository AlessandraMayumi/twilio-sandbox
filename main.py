import uvicorn
from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse

from db.conn import connect

app = FastAPI()


@app.post("/")
async def receive_message_from_sandbox(request: Request):
    params = request.query_params
    sender = params.get('From')
    receiver = params.get('To')
    msg = params.get('Body')

    col = connect()
    if not col.find_one(filter={'from':sender}):
        col.insert_one({'from': sender, 'to': receiver, 'msg': [msg]})
    col.update_one({'from': sender}, {'$push': {msg}})

    resp = MessagingResponse()
    response_msg = resp.message()
    response_msg.body(f'Two-way message')

    return str(resp)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
