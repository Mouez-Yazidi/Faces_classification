# Face Classification Model Deployment using FastAPI

This repository contains a face classification model deployment using FastAPI. With this project, you can easily classify faces in images using a pre-trained machine learning model. 
this model is able to classify faces into 5 classes :
 1. age  
 2. ethnitcity  
 3. gender
 4. eye ( open or closed)
 5. hair classification (straight /curly /bald)
 6. Tone color

This README provides instructions for setting up the project environment and making predictions using the FastAPI application.


## Prerequisites

Before you get started, ensure that you have the following prerequisites installed:

1. **Python**: You will need Python installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

2. **Virtual Environment**: It's a good practice to create a virtual environment to manage project dependencies. You can create a virtual environment using Python's built-in `venv` module or install `virtualenv`.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Mouez-Yazidi/Faces_classification.git
   cd Faces_classification

2. Create a virtual environment named `face_processing` and activate it Using venv (Python 3.3+):

  ```bash
  python -m venv face_processing
  face_processing\Scripts\activate
  ```

3. Install the required packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```
**Note:** that maybe take some minutes based on your internet connexion

4. start the api using this command :
   ```python
   python main.py

5. now, you can make prediction using the web interface of fastapi, all you need is the open you browser and access to this url : http://localhost:8000/docs#/prediction/
