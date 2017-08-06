
import traceback
import logging.config
import config
import random
from datetime import datetime
from polly_mp3 import PollyMp3
from twilio_polly import TwilioPolly

logger = logging.getLogger()

if config.logger_level == 'INFO':
    logger.setLevel(logging.INFO)
elif config.logger_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif config.logger_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    try:

        polly = PollyMp3()
        twilio = TwilioPolly()
        tel_number = event['tel']
        if tel_number[0:1] == '0':
            tel_number = '+81' + tel_number[1:len(tel_number)]

        file_name = '{tel}{time}'.format(
            tel=tel_number.replace('+',''),
            time=datetime.now().strftime('%Y%m%d%H%M%S')
        )
        mp3_url = polly.set_mp3(
            file_name,
            '{message_0} , {message_1}'.format(
                message_0=config.message_prefix,
                message_1=random.choice(config.messages)
            )
        )
        logger.info(mp3_url)

        twiml_str = twilio.get_twiml(mp3_url)
        logger.info(twiml_str)

        twiml_url = polly.set_twiml(file_name, twiml_str)
        logger.info(twiml_url)

        call_sid = twilio.make_call(tel_number, twiml_url)
        logger.info(call_sid)

        message = twilio.send_message(tel_number)
        logger.info(message)

        return {
            'call_sid': call_sid,
            'message': message,
            'tel_number': tel_number
        }

    except Exception as e:
        raise Exception(traceback.format_exc())
