import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

LEFT_EYE = [33, 160, 158, 133, 153, 144]

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

def check_blink(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if not result.multi_face_landmarks:
        return False

    h, w, _ = frame.shape

    for face in result.multi_face_landmarks:
        eye = []
        for idx in LEFT_EYE:
            x = int(face.landmark[idx].x * w)
            y = int(face.landmark[idx].y * h)
            eye.append([x, y])

        eye = np.array(eye)
        ear = eye_aspect_ratio(eye)

        if ear < 0.2:  # mắt đóng
            return True

    return False