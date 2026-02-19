from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()
model = YOLO("yolov8n-pose.pt")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    img_bytes = await file.read()
    np_img = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = model(frame, verbose=False)

    distress = False
    persons = 0

    if results[0].keypoints is not None:
        persons = len(results[0].keypoints)
        for kp in results[0].keypoints.data.cpu().numpy():
            lw, rw = kp[9], kp[10]
            ls, rs = kp[5], kp[6]
            if lw[1] < ls[1] and rw[1] < rs[1]:
                distress = True

    return {
        "distress": distress,
        "persons": persons
    }


#how to run API
#uvicorn api:app --host 0.0.0.0 --port 8000

#how to active ven
#venv\Scripts\Activate
