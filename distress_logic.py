from mediapipe.solutions.pose import PoseLandmark

class DistressDetector:
    def is_hand_raised(self, landmarks):
        left_wrist = landmarks[PoseLandmark.LEFT_WRIST]
        left_shoulder = landmarks[PoseLandmark.LEFT_SHOULDER]

        right_wrist = landmarks[PoseLandmark.RIGHT_WRIST]
        right_shoulder = landmarks[PoseLandmark.RIGHT_SHOULDER]

        if left_wrist.y < left_shoulder.y:
            return True
        if right_wrist.y < right_shoulder.y:
            return True

        return False
