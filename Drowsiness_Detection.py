import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist
from pygame import mixer

# -----------------------------
# SOUND ALERT
# -----------------------------
mixer.init()
mixer.music.load("music.wav")

# -----------------------------
# MEDIAPIPE FACE MESH SETUP
# -----------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,       # For detailed eye landmarks
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Eye landmark IDs (MediaPipe numbers)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# EAR calculation function
def eye_aspect_ratio(landmarks, eye_points):
    pts = np.array([(landmarks[p].x, landmarks[p].y) for p in eye_points])

    A = dist.euclidean(pts[1], pts[5])
    B = dist.euclidean(pts[2], pts[4])
    C = dist.euclidean(pts[0], pts[3])

    ear = (A + B) / (2.0 * C)
    return ear

# -----------------------------
# PARAMETERS
# -----------------------------
EAR_THRESHOLD = 0.25
FRAME_THRESHOLD = 15
sleep_counter = 0

# -----------------------------
# CAMERA START
# -----------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]

        leftEAR = eye_aspect_ratio(face.landmark, LEFT_EYE)
        rightEAR = eye_aspect_ratio(face.landmark, RIGHT_EYE)
        ear = (leftEAR + rightEAR) / 2.0

        # Draw eye landmarks
        for id in LEFT_EYE + RIGHT_EYE:
            x = int(face.landmark[id].x * w)
            y = int(face.landmark[id].y * h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Drowsiness detection
        if ear < EAR_THRESHOLD:
            sleep_counter += 1

            if sleep_counter > FRAME_THRESHOLD:
                cv2.putText(frame, "ALERT! WAKE UP!!", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                mixer.music.play()
        else:
            sleep_counter = 0

        cv2.putText(frame, f"EAR: {ear:.2f}", (20, h - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Drowsiness Detection (MediaPipe)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()