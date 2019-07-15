from accessToken import getAccessToken
from slack import getImageUrlForSlack
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
	location = {"lat": 35.658034, "lon": 139.701636} # 渋谷スクランブル交差点
	ping = s.post("https://api.gotinder.com/v2/meta",
				 params=json.dumps(params))
	count=0
	while count < 101:
		# 周囲のユーザーを取得
		users = s.post("https://api.gotinder.com/user/recs")
		for user in json.loads(users.text)["results"]:
			id = user["_id"]
			# 右スワイプ
			s.get("https://api.gotinder.com/like/{}".format(id))
			print(user["name"],"❤️")
			text = "あへぇ"
			getImageUrlForSlack(text)
			# FIXME: Slackの通知がまだうまく行かない
			count+=1
			if count == 100:
				print("done!!")
	
	# TODO: Firebase使って画像保存

  # NOTE: 以下はやりたいこと。25歳以下だけスワイプとか、写真を何枚か取得するとか色々。
	# FIXME: エラーが出るのでコメントアウト。（そのうちいらなくなって消すかも）

	# 周囲のユーザーを取得
	# users = s.post("https://api.gotinder.com/user/recs")
	# userList = []
	# for user in json.loads(users.text)["results"]:
	# 	# print(user["photos"])
	# 	userInfo = []
	# 	userInfo.append(user["name"])
	# 	userInfo.append(user["_id"])
	# 	id = user["_id"]
	# 	userInfo.append(user["distance_mi"])
	# 	age = user["distance_mi"]
	# 	for image in user["photos"]:
	# 		# print(image["url"])
	# 		# userInfo.append(image["url"])

	# 		image = image['url']
	# 		if image.endswith(".webp"):
	# 			image = image.replace(".webp",".jpg")
	# 			userInfo.append(image)
	# 		# 右スワイプ
	# 		if image is not None and age <= 25:
	# 			s.get("https://api.gotinder.com/like/{}".format(id))
	# 			userInfo.append("Liked")
	# 	userList.append(userInfo)
			
	# for user in userList:
	# 	print(user)
