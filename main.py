import uvicorn
from fastapi import FastAPI,File,UploadFile
from prediction import prediction_details
import cv2
import numpy
app = FastAPI()

@app.post("/prediction/")
def prediction(file: UploadFile = File(...)):
    try:
        if file.content_type.startswith('image/'):
            # Read the uploaded image using OpenCV
            image = cv2.imdecode(np.fromstring(file.file.read(), np.uint8), cv2.IMREAD_COLOR)

            # Process the image (you can add your image processing code here)
            # For example, you can save the image or perform some image analysis.
            prediction = prediction_details(image)
            return {"filename": file.filename, "prediction": prediction}
        else:
            return {"error": "Only image files are allowed."}
    except Exception as e:
        return {"error":e}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
