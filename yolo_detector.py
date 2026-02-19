from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # ringan & cepat

    def detect_persons(self, frame):
        results = self.model(frame, conf=0.4, classes=[0], verbose=False)
        boxes = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))

        return boxes
