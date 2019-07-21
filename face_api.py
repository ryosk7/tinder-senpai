import requests, json
import os
from os.path import join, dirname
from dotenv import load_dotenv
import cognitive_face as CF

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
  faces = CF.face.detect(face_image_url)
  print(faces)