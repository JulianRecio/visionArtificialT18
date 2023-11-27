import face_recognition
import cv2
import os
import ast
import numpy as np

def generate_face_encodings(folder_path):
 encodings = []
 filenames = []
 booleans = []

 # Loop over all files in the folder
 for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'): # Add more conditions if you have other image formats
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

        # Append a boolean value to the booleans list
        booleans.append(False)

 # Save the arrays in a .txt file
 with open('encodings.txt', 'w') as f:
    for encoding in encodings:
        f.write(str(encoding) + '\n')

 with open('filenames.txt', 'w') as f:
    for name in filenames:
        f.write(name + '\n')

 with open('booleans.txt', 'w') as f:
    for boolean in booleans:
        f.write(str(boolean) + '\n')


def split_encodings(encodings):
    return [encodings[i:i + 128] for i in range(0, len(encodings), 128)]


def read_data_from_encodings_list(file_path):
    encodings = []

    with open(file_path, 'r+') as file:
        for line in file:
            # Remove unwanted characters and split the line into tokens
            tokens = ''.join(c if c.isdigit() or c in ['.', '-'] else ' ' for c in line).split()
            for token in tokens:
                number = float(token)
                encodings.append(number)

    return split_encodings(encodings)



def read_data_from_txt_files():
 # Read the data from the .txt files
    encodings = read_data_from_encodings_list('finalProject/encodings.txt')

    with open('finalProject/filenames.txt', 'r+') as f:
        filenames = [line.strip() for line in f.readlines()]

    with open('finalProject/booleans.txt', 'r+') as f:
        booleans = [ast.literal_eval(line.strip()) for line in f.readlines()]

        # Convert the list of encodings to a numpy array

    return encodings, filenames, booleans

def find_attendance(best_match_index, attendance):
    if 0 <= best_match_index < len(attendance):
        element = attendance[best_match_index]
    return element


def check_in(best_match_index, attendance):
    attendance[best_match_index] = True
    return attendance


def overwrite_attendancde(attendance):
    with open('finalProject/booleans.txt', 'w') as f:
        for boolean in attendance:
            f.write(str(boolean) + '\n')