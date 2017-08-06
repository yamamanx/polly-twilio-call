
import logging
import traceback
import config
from boto3 import Session
from boto3 import resource
from contextlib import closing

logger = logging.getLogger()

if config.logger_level == 'INFO':
    logger.setLevel(logging.INFO)
elif config.logger_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif config.logger_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)


class PollyMp3(object):

    def __init__(self):
        self.polly_region = config.polly_region
        self.bucket_name = config.bucket_name
        self.bucket_region = config.bucket_region
        self.voice_id = config.voice_id

    def set_twiml(self, file_name, twiml_str):
        try:
            s3 = resource('s3')
            bucket = s3.Bucket(self.bucket_name)

            twiml_file_name = '%s.xml' % file_name

            bucket.put_object(
                Key=twiml_file_name,
                Body=twiml_str,
                ContentType='application/xml'
            )

            ENTRY_URL = "https://s3-{region}.amazonaws.com/{bucket}/{filename}"
            entry_url = ENTRY_URL.format(
                bucket=self.bucket_name,
                region=self.bucket_region,
                filename=twiml_file_name
            )

            return entry_url

        except Exception as e:
            raise Exception(traceback.format_exc())

    def set_mp3(self, file_name, polly_text):
        try:
            session = Session(region_name=self.polly_region)
            polly = session.client("polly")
            s3 = resource('s3')
            bucket = s3.Bucket(self.bucket_name)

            response = polly.synthesize_speech(
                Text=polly_text,
                OutputFormat="mp3",
                VoiceId=self.voice_id)

            mp3_file_name = '%s.mp3' % file_name

            with closing(response["AudioStream"]) as stream:
                bucket.put_object(
                    Key=mp3_file_name,
                    Body=stream.read(),
                    ContentType = 'audio/mpeg'
                )

            ENTRY_URL = "https://s3-{region}.amazonaws.com/{bucket}/{filename}"
            entry_url = ENTRY_URL.format(
                bucket=self.bucket_name,
                region=self.bucket_region,
                filename=mp3_file_name
            )

            return entry_url

        except Exception as e:
            raise Exception(traceback.format_exc())