import threading
import cv2
from deepface import DeepFace

# Capturar video y mostrar
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
# FIja el frame en 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# Como no queremos contar matches cada frame, agregamos el counter
counter = 0
#
face_match = True

reference_img = cv2.imread("JulianRecio.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0), 3)
        else:
            cv2.putText(frame, "No Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3)

        cv2.imshow("video", frame)


    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()