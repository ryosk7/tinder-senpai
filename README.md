# tinderパイセン
## tinderパイセンとは
忙しいけど彼女が欲しいあなたのために、たくさんの女の子をLIKEしてくれる
とても優しい先輩なのだ！！
※ 必ずマッチするとは限りません。
### (至高のtinder性活を送るための)Setup
```sh
$ docker-compose build
$ docker-compose run oppai sh
(コンテナ内)
$ pipenv install
```
### 焦らないで！あと少しで女の子とマッチングできるよ！
.envを作成。(.env.sampleのように作成する)
以下を記入。
```.env
FB_EMAIL="○○○○.samplemail.com"
FB_PASS="○○○○○○○○○○○○○○○"
SLACK_WEB_HOOK_ENDPOINT="○○○○○○○○○○○○○○○○○○○"
FACE_API_TOKEN="○○○○○○○○○○○○○○○○○○○"
```
FB_EMAILは、Facebookに登録されているメール。
FB_PASSは、Facebookに登録されているパスワード。
SLACK_WEB_HOOK_ENDPOINTは、Slackのアプリからincoming-webhookをインストールすると、生成されるURL。
「https://hooks.slack.com/services/○○○○○○○○○○○○○○○○○○○」の○○○部分を記入する。
FACE_API_TOKENは、Face Apiのトークン。これを設定することで、顔の判定を行う。
### さぁ！女の子と出会おう！！
```
(コンテナ内)
$ pipenv run start
```
tinder.pyの中にあるlocationを変更することで、探してくれる場所を帰ることができるよ！
あと、tinderに課金しとくといいかもね！