import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to convert an image to a sketch
def convert_to_sketch(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    
    # Blur the inverted image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred
    
    # Create the pencil sketch image
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    
    return sketch_image

# Streamlit app
st.title("Image to Sketch Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Convert the uploaded image to an OpenCV image
    image = np.array(image.convert('RGB'))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    st.write("Converting to sketch...")

    # Convert the image to a sketch
    sketch_image = convert_to_sketch(image)

    # Display the sketch image
    st.image(sketch_image, caption='Sketch Image.', use_column_width=True, channels='GRAY')
