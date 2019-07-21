from accessToken import getAccessToken
from slack import getImageUrlForSlack
from face_api import checkFaceApi
from dotenv import load_dotenv
import os
from os.path import join, dirname
import requests
import json

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

FBemail = os.environ.get("FB_EMAIL")
FBpass = os.environ.get("FB_PASS")

#FBトークンの取得
token = getAccessToken(FBemail, FBpass)

# Tinderのトークンの取得
with requests.Session() as s:
	params = {"token": token}
	response = s.post(
		"https://api.gotinder.com/v2/auth/login/facebook", data=json.dumps(params))
	print(response.text)
	response = json.loads(response.text)
	api_token = response["data"]["api_token"]

	# Tinderのヘッダーをセット
	headers = {"X-Auth-Token": api_token, "Content-type": "application/json",
							"User-agent": "Tinder/10.1.0 (iPhone; iOS 12.1; Scale/2.00)"}
	s.headers.update(headers)

	# 位置情報の登録
	location = {"lat": 35.684669, "lon": 139.697098} # ギークハウス新宿の緯度・経度
	ping = s.post("https://api.gotinder.com/v2/meta",
				 params=json.dumps(params))
	count = 0
	while count < 101:
		# 周囲のユーザーを取得
		users = s.post("https://api.gotinder.com/user/recs")
		for user in json.loads(users.text)["results"]:
			id = user["_id"]
			for image in user["photos"]:
				sendImage = ''
				image = image['url']
				if image.endswith(".webp"):
					sendImage = image.replace(".webp",".jpg") #.webpを.jpgに変換
				if sendImage is not '':
					checkFaceApi(sendImage)
				getImageUrlForSlack(sendImage)
			# 右スワイプ
			s.get("https://api.gotinder.com/like/{}".format(id))
			print(user["name"],"❤️")
			count += 1
	
# TODO: Firebase使って画像保存
# NOTE: 以下はやりたいこと。25歳以下だけスワイプとか、写真を何枚か取得するとか色々。
