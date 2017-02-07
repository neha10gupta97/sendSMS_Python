from twilio.rest import TwilioRestClient
from credential import account_sid, auth_token, sendto, twilio_no


client = TwilioRestClient(account_sid,auth_token)

client.messages.create(from_=twilio_no,
                        to=sendto,
                        body="Hii!! here:D")
