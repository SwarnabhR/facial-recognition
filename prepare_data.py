import face_recognition
import os
import pickle

def load_and_encode_images(image_dir):
    encodings = []
    names = []
    
    for person_name in os.listdir(image_dir):
        person_folder = os.path.join(image_dir,person_name)
        if not os.path.isdir(person_folder):
            continue
        
        for image_file in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_file)