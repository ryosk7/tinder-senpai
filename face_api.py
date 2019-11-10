import requests, json
import os
from os.path import join, dirname
from dotenv import load_dotenv
import cognitive_face as CF
import time
import cv2

face_cascade_path = '/usr/local/opt/opencv/share/'\
                    'OpenCV/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/usr/local/opt/opencv/share/'\
                   'OpenCV/haarcascades/haarcascade_eye.xml'

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


def checkFaceToOpenCV(face_image_url):
  face_list = []
  judges = 0
  for face_image in face_image_url:
    if face_image is not '':
      faces = cv2.imread(face_image)
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

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

src = cv2.imread('data/src/lena_square.png')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
  cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
  face = src[y: y + h, x: x + w]
  face_gray = src_gray[y: y + h, x: x + w]
  eyes = eye_cascade.detectMultiScale(face_gray)
  for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imwrite('data/dst/opencv_face_detect_rectangle.jpg', src)