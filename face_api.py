import requests, json
import os
from os.path import join, dirname
from dotenv import load_dotenv
import cognitive_face as CF
import time

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

face_api_token = os.environ.get("FACE_API_TOKEN")

# Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(face_api_token)

# Replace with your regional Base URL
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
def checkFaceApi(face_image_url):
  face_list = []
  judges = 0
  for face_image in face_image_url:
    if face_image is not '':
      faces = CF.face.detect(face_image)
      face_list.append(faces)
      time.sleep(1)
  for face in face_list:
    if face is 0:
      judges += 0
    else:
      judges += 1
  if judges > 0:
    return True
  else:
    return False