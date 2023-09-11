import cv2
import numpy as np

def nothing(x):
    pass

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Cargar las imágenes de referencia en color y convertirlas a escala de grises
reference_image1 = cv2.imread("estrella.png")
gray_reference1 = cv2.cvtColor(reference_image1, cv2.COLOR_BGR2GRAY)
_, threshold_reference1 = cv2.threshold(gray_reference1, 100, 255, cv2.THRESH_BINARY)
contours_reference1, _ = cv2.findContours(threshold_reference1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_reference1 = sorted(contours_reference1, key=cv2.contourArea, reverse=True)
reference_contour1 = contours_reference1[0]

reference_image2 = cv2.imread("Circulo.png")
gray_reference2 = cv2.cvtColor(reference_image2, cv2.COLOR_BGR2GRAY)
_, threshold_reference2 = cv2.threshold(gray_reference2, 100, 255, cv2.THRESH_BINARY)
contours_reference2, _ = cv2.findContours(threshold_reference2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_reference2 = sorted(contours_reference2, key=cv2.contourArea, reverse=True)
reference_contour2 = contours_reference2[0]

# Crear ventanas para ajustar los parámetros
cv2.namedWindow("Ajustes")
cv2.namedWindow("Contorno de Referencia 1")
cv2.namedWindow("Contorno de Referencia 2")
cv2.createTrackbar("Umbral", "Ajustes", 100, 255, nothing)
cv2.createTrackbar("Tamaño del Elemento Estructural", "Ajustes", 0, 50, nothing)
cv2.createTrackbar("Mínimo Área", "Ajustes", 100, 5000, nothing)
cv2.createTrackbar("Máximo Área", "Ajustes", 5000, 10000, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Obtener los valores actuales de los parámetros desde las barras de desplazamiento
    threshold_value = cv2.getTrackbarPos("Umbral", "Ajustes")
    kernel_size = cv2.getTrackbarPos("Tamaño del Elemento Estructural", "Ajustes")
    min_area = cv2.getTrackbarPos("Mínimo Área", "Ajustes")
    max_area = cv2.getTrackbarPos("Máximo Área", "Ajustes")

    _, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    annotated_frame = frame.copy()

    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            match1 = cv2.matchShapes(reference_contour1, contour, cv2.CONTOURS_MATCH_I1, 0)
            match2 = cv2.matchShapes(reference_contour2, contour, cv2.CONTOURS_MATCH_I1, 0)
            if match1 < 0.01:
                color = (0, 255, 0)  # Color para los contornos similares a la referencia 1
            elif match2 < 0.01:
                color = (0, 0, 255)  # Color para los contornos similares a la referencia 2
            else:
                color = (255, 0, 0)  # Color para otros contornos
            cv2.drawContours(annotated_frame, [contour], -1, color, 2)

    cv2.imshow("Detección de Contornos Similares", annotated_frame)
    cv2.imshow("Imagen en Blanco y Negro", threshold)
    cv2.imshow("Contorno de Referencia 1", cv2.drawContours(np.zeros_like(frame), [reference_contour1], -1, (255, 255, 255), 2))
    cv2.imshow("Contorno de Referencia 2", cv2.drawContours(np.zeros_like(frame), [reference_contour2], -1, (255, 255, 255), 2))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()