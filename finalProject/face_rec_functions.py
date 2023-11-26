import face_recognition
import cv2
import os
def generate_face_encodings(folder_path):
   encodings = []
   filenames = []

   # Loop over all files in the folder
   for filename in os.listdir(folder_path):
       if filename.endswith('.jpg') or filename.endswith('.png'):  # Add more conditions if you have other image formats
           # Construct the full file path
           file_path = os.path.join(folder_path, filename)

           # Load the image file
           image = face_recognition.load_image_file(file_path)

           # Convert the image to RGB format
           image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

           # Get the face encodings for the first face found in the image
           face_encoding = face_recognition.face_encodings(image)[0]

           # Add the face encoding to the list
           encodings.append(face_encoding)

           # Split the filename into the first name, last name, and date
           first_name, last_name = filename.split('_')

           # Remove the file extension from the last name
           last_name = os.path.splitext(last_name)[0]

           # Append the first and last names to the filenames list
           filenames.append(first_name + ' ' + last_name)

   return encodings, filenames