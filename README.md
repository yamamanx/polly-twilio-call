# 作成中

# Polly Twilio Call

* リクエストされた電話番号にリストからランダムで生成したスマートフォン川柳をPollyで音声に変換して電話をかけます。
* SMSへ広告のメッセージを送信します。


## AWS Lambda

- ソースコードをダウンロードして、requirements.txtに記載のパッケージをソースコードと同じフォルダにインストールしてzipで固めて、Lambdaにアップロードします。


## AWS Lambdaに設定する環境変数

変数名|設定値
:--|:--
BUCKET_NAME|Amazon Pollyが生成するMP3ファイルを格納するS3バケット名
BUCKET_REGION|ap-northeast-1など S3バケットがあるリージョン名
VOICE_ID|Amazon PollyのボイスID 日本語なので Mizukiを設定する
POLLY_REGION|Amazon Pollyのリージョン名
TWILIO_ACCOUNT_SID|TwilioのアカウントSID
TWILIO_AUTH_TOKEN|Twilioのトークン
TWILIO_FROM_NUMBER|Twilioの発信元電話番号