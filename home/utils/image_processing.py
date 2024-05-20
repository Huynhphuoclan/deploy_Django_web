import os
import cv2
import numpy as np
import imageio.v2 as imageio
from joblib import load

def process_image_file(image_file):
    image = imageio.imread(image_file)
    resized_image = cv2.resize(image, (32, 32))
    return resized_image

def preprocess_images(images):
    preprocessed_images = []
    for image in images:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        normalized_image = grayscale_image.astype(np.float32) / 255.0
        cropped_image = normalized_image[4:28, 5:27]
        flattened_image = cropped_image.flatten()
        preprocessed_images.append(flattened_image)
    preprocessed_images = np.array(preprocessed_images)
    return preprocessed_images

def predict_images(images):
    model_path = os.path.join('model', 'rf_model_finetuned.joblib')
    loaded_model = load(model_path)
    predictions = loaded_model.predict(images)
    return predictions