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
.envを作成。
以下を記入。
```.env
FB_EMAIL = "○○○○.samplemail.com"
FB_PASS = "○○○○○○○○○○○○○○○"
SLACK_WEB_HOOK_URL = "https://hooks.slack.com/services/○○○○○○○○○○○○○○○○○○○"
```
FB_EMAILはFacebookに登録されているメール。
FB_PASSはFacebookに登録されているパスワード。
SLACK_WEB_HOOK_URLはSlackのアプリからincoming-webhookをインストールすると、生成されるURL。
### さぁ！女の子と出会おう！！
```
(コンテナ内)
$ python tinder.py
```
tinder.pyの中にあるlocationを変更することで、探してくれる場所を帰ることができるよ！
あと、tinderに課金しとくといいかもね！