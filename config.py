# coding:utf-8

import os

logger_level = os.environ['LOGGER_LEVEL']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_from_number = os.environ['TWILIO_FROM_NUMBER']
bucket_name = os.environ['BUCKET_NAME']
bucket_region = os.environ['BUCKET_REGION']
voice_id = os.environ['VOICE_ID']
polly_region = os.environ['POLLY_REGION']


message_body = u'SIMの見直しでこんなにもお得\n' \
               u'mineo紹介キャンペーン\n' \
               u'Amazonギフト券2,000円をプレゼント\n' \
               u'https://www.yamamanx.com/iphone-se-sim-free-mineo/'

message_prefix = u'サラリーマン川柳 スマートフォン編'

messages = [
    u'スマートフォン , 使う妻とは , 不話不音',
    u'妻のグチ , ツイッターなら , つぶやける',
    u'ツイッター , 私が言っても , ひとりごと',
    u'部下からの , 遅刻のメール , 渋滞なう',
    u'アイウォンチュー , いつでも君は , アイフォン中',
    u'アイパッド , 目に貼る物かと , 聞く親父',
    u'スマートフォン , 名前がいやみと , 妻が言う',
    u'つい言った , 無口な僕も , ツイッター',
    u'図書館で , フェイスブックを , さがす父',
    u'地図アプリ , ひらいてなやむ , ここはどこ',
    u'スマホより , トクホが先と , 妻が言う',
    u'妻よ！子よ！ , ワシより大事か？！ , そのスマホ',
    u'オレの指 , スマホも部下も , 動かせず'
]