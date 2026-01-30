import cv2
from blink_liveness import check_blink
from face_recognition_lbph import recognize_face
from attendance import save_attendance

cap = cv2.VideoCapture(0)
liveness_ok = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Khong mo duoc camera")
        break

    if not liveness_ok:
        cv2.putText(frame, "Vui long nhay mat", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if check_blink(frame):
            liveness_ok = True
            print("Liveness passed")

    else:
        name = recognize_face(frame)
        if name != "Unknown":
            save_attendance(name)
            break

    cv2.imshow("He thong cham cong", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()