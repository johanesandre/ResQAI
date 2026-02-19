import cv2
import time
import numpy as np
import winsound
from ultralytics import YOLO

# =====================
# CONFIG
# =====================
BEEP_FREQ = 1200   # Hz
BEEP_DURATION = 300  # ms
ALARM_INTERVAL = 0.35  # detik (agar beep terus tapi tidak terlalu rapat)

# =====================
# INIT
# =====================
model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture(0)

last_beep_time = 0

# =====================
# HELPER FUNCTIONS
# =====================
def draw_bbox(frame, box):
    x1, y1, x2, y2 = map(int, box)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

def draw_body(frame, kps):
    skeleton = [
        (5, 7), (7, 9),     # left arm
        (6, 8), (8, 10),    # right arm
        (5, 6),             # shoulders
        (5, 11), (6, 12),   # body
        (11, 12),
        (11, 13), (13, 15),
        (12, 14), (14, 16)
    ]

    for i, j in skeleton:
        if kps[i][2] > 0.5 and kps[j][2] > 0.5:
            x1, y1 = int(kps[i][0]), int(kps[i][1])
            x2, y2 = int(kps[j][0]), int(kps[j][1])
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

def both_hands_raised(kps):
    left_wrist = kps[9]
    right_wrist = kps[10]
    left_shoulder = kps[5]
    right_shoulder = kps[6]

    if (
        left_wrist[2] > 0.5 and right_wrist[2] > 0.5 and
        left_shoulder[2] > 0.5 and right_shoulder[2] > 0.5
    ):
        return (
            left_wrist[1] < left_shoulder[1] and
            right_wrist[1] < right_shoulder[1]
        )
    return False

# =====================
# MAIN LOOP
# =====================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)

    distress_detected = False

    if results[0].keypoints is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        keypoints = results[0].keypoints.data.cpu().numpy()

        for box, kp in zip(boxes, keypoints):
            draw_bbox(frame, box)
            draw_body(frame, kp)

            if both_hands_raised(kp):
                distress_detected = True
                cv2.putText(
                    frame,
                    "NEED HELP !!",
                    (int(box[0]), int(box[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    3
                )

    # =====================
    # ALARM LOGIC
    # =====================
    current_time = time.time()
    if distress_detected:
        if current_time - last_beep_time > ALARM_INTERVAL:
            winsound.Beep(BEEP_FREQ, BEEP_DURATION)
            last_beep_time = current_time

    cv2.imshow("Flood & Emergency Rescue AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
