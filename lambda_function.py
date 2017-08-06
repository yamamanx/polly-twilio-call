
import traceback
import logging
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


def main(event, context):
    try:

        polly = PollyMp3()
        twilio = TwilioPolly()
        tel_number = event['tel']
        if tel_number[0:1] == '0':
            tel_number = '+81' + tel_number[1:len(tel_number)]

        file_name = '{tel}{time}'.format(
            tel=tel_number,
            time=datetime.now.strftime('%Y%m%d%H%M%S')
        )
        mp3_url = polly.set_mp3(
            file_name,
            random.choice(config.response_message)
        )
        logger.info(mp3_url)

        twiml_str = twilio.get_twiml(mp3_url)
        logger.info(twiml_str)

        twiml_url = polly.set_twiml(file_name, twiml_str)
        logger.info(twiml_url)

        call_sid = twilio.make_call(tel_number, twiml_url)
        logger.info(call_sid)

    except Exception as e:
        logger.error(traceback.format_exc())


def lambda_handler(event, context):
    logger.setLevel(logging.INFO)
    main(event, context)
    return {
        'message': 'done'
    }

if __name__ == '__main__':
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    event = {}
    main(event, None)