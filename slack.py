import requests, json
import os
from os.path import join, dirname
from dotenv import load_dotenv

endpoint = "SLACK_WEB_HOOK_ENDPOINT"
WEB_HOOK_URL = "https://hooks.slack.com/services/{}".format(endpoint)

def getImageUrlForSlack(imageUrl):
  requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': imageUrl,  #通知内容
    'username': u'tinder先輩',  #ユーザー名
    'icon_emoji': u':smile_cat:',  #アイコン
    'link_names': 1,  #名前をリンク化
  }))