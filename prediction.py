import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
from io import BytesIO

def prediction_details(img):

    color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        #this analyses the given image and gives values
        prediction = DeepFace.analyze(color_img, actions=['age', 'gender','race'])
        return {
            "gender":prediction[0]['dominant_gender'],
            "race":prediction[0]['dominant_race'],
            "age":prediction[0]['age']
            }
    except:
        return "no face detected"
