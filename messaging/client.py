import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_message(receiver_number):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Hello from Twilio',
        to='whatsapp:+' + receiver_number
    )

    print(message.sid)
