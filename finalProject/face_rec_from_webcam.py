import face_recognition
import cv2
import numpy as np
import face_rec_functions

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Function to generate embeddings and names. Ideally, these should be .txt files or something else
known_face_encodings, known_face_names, attendance = face_rec_functions.read_data_from_txt_files()


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        color = (0, 0, 255)
        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        attended_event = face_rec_functions.find_attendance(best_match_index, attendance)

        if matches[best_match_index] & attended_event == False:
            name = known_face_names[best_match_index]
            color = (0,255,0)

        if matches[best_match_index] & attended_event == True:
            name = known_face_names[best_match_index]
            color = (0,255,255)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            attendance = face_rec_functions.check_in(best_match_index, attendance)
            cv2.waitKey(-1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_rec_functions.overwrite_attendancde(attendance)
            break
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        face_rec_functions.overwrite_attendancde(attendance)
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()