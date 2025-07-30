import cv2 as cv
from ultralytics import YOLO
import math
# # Open camera
# cam = cv.VideoCapture(0)
# cam.set(cv.CAP_PROP_FRAME_WIDTH, 1280)  # Set width to 1280
# cam.set(cv.CAP_PROP_FRAME_HEIGHT, 720)  # Set height to 720
# Use a video file instead of camera
cam = cv.VideoCapture('../video/Test_video.mp4') #comment this line to use camera

model = YOLO('../model/model01.pt') 

try:
    while True:
        success, img = cam.read()
        # set img to a fixed size
        height, width = img.shape[:2]
        img = cv.resize(img, (width // 2, height // 2))
        if not success:
            print("Failed to read from camera or video file.")
            break
        results = model(img, stream=True)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])

                if conf >= 0.50:
                    cropped = img[y1:y2, x1:x2]
                    cv.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv.putText(img, f'Class: {cls}, Conf: {conf}', (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv.imshow("YOLO", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Exiting program...")