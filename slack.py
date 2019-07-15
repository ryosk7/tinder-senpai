import requests, json
import os
from os.path import join, dirname
from dotenv import load_dotenv

WEB_HOOK_URL = "SLACK_WEB_HOOK_URL"

def getImageUrlForSlack(imageUrl):
  requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': u'{imageUrl}',  #通知内容
    'username': u'tinder先輩',  #ユーザー名
    'icon_emoji': u':smile_cat:',  #アイコン
    'link_names': 1,  #名前をリンク化
  }))