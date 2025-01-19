from twilio.rest import Client

# Twilio credentials from your Twilio account
account_sid = '###'
auth_token = '###'

client = Client(account_sid, auth_token)

call = client.calls.create(
    to='+16134007249',  # Phone number you want to call
    from_='+15075027627',  # Your Twilio number
    url='http://demo.twilio.com/docs/voice.xml'  # The Twilio Voice URL (XML file)
)

print(f"Call initiated: {call.sid}")
