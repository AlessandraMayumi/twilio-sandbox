import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello Twilio Client',
        to='whatsapp:+5519989711675'
    )

    print(message.sid)
