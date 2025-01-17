# pip install opencv-python-headless ultralytics cryptography

from ultralytics import YOLO
import cv2
import base64
import numpy as np

model = YOLO("yolov8n.pt")
img_path = "./호나우지뉴.JPG"
# img = np.frombuffer(base64.b64decode(img_path), np.uint8)
img = cv2.imread(img_path)
# frame = cv2.imdecode(img, cv2.IMREAD_COLOR)
frame = cv2.resize(img, (320, 320))

result = model(frame)
annotated_frame = result[0].plot(show=False)
cv2.imwrite('./output.JPG', annotated_frame)