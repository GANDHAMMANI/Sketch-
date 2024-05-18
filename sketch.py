import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to convert an image to a sketch
def convert_to_sketch(image, ksize):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    
    # Blur the inverted image
    blurred = cv2.GaussianBlur(inverted_image, (ksize, ksize), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred
    
    # Create the pencil sketch image
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    
    return sketch_image

# Ensure ksize is an odd number
def ensure_odd(ksize):
    if ksize % 2 == 0:
        return ksize + 1
    return ksize

# Streamlit app
st.title("Image to Sketch Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image.convert('RGB'))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Display original image on the right side
    col1, col2 = st.columns(2)
    col1.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.header("Adjust Sketch Settings")
    
    # Slider for the user to adjust blur intensity
    ksize = st.slider("Blur Intensity", min_value=1, max_value=200, step=1, value=21)
    
    # Ensure the kernel size is odd
    ksize = ensure_odd(ksize)
    
    st.sidebar.write("Note: Higher values produce smoother sketches.")

    st.write("Converting to sketch...")

    try:
        # Convert the image to a sketch
        sketch_image = convert_to_sketch(image, ksize)
        
        # Display the sketch image on the left side
        col2.image(sketch_image, caption='Sketch Image', use_column_width=True, channels='GRAY')

   
    except Exception as e:
        st.error(f"An error occurred: {e}")
