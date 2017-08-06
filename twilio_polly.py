
import config
import logging
import traceback
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

logger = logging.getLogger()

if config.logger_level == 'INFO':
    logger.setLevel(logging.INFO)
elif config.logger_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif config.logger_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)

class TwilioPolly(object):

    def __init__(self):
        self.account_sid = config.twilio_account_sid
        self.auth_token = config.twilio_auth_token
        self.from_number = config.twilio_from_number

    def get_twiml(self, entry_url):
        resp = VoiceResponse()
        resp.play(entry_url)

        return str(resp)

    def make_call(self, to_number, twiml_url):
        try:
            client = Client(self.account_sid, self.auth_token)
            call = client.api.account.calls.create(
                to=to_number,
                from_=self.from_number,
                url=twiml_url,
                method='GET'
            )

            return call.sid

        except Exception as e:
            raise Exception(traceback.format_exc())

    def send_message(self, to_number):
        try:
            client = Client(self.account_sid, self.auth_token)
            message = client.api.account.messages.create(
                to=to_number,
                from_=self.from_number,
                body=config.message_body
            )

            return message.sid

        except Exception as e:
            raise Exception(traceback.format_exc())
