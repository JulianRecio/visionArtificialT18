import cv2
from real_time_face_recon_functions import detect_bounding_box

# Considerar usar arcface

# Accedemos a la camara
video_capture = cv2.VideoCapture(0)

while True:

    result, video_frame = video_capture.read()  # Leemos los frames del video
    if result is False:
        break

    faces = detect_bounding_box(
        video_frame
    )  # Aplicamos la función que creamos al frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # Mostramos la deteccion en una ventana

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()