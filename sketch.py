import streamlit as st
from sketchpy import canvas as gfg
from PIL import Image

def main():
    st.title("Image to Sketch Converter")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image.', use_column_width=True)
        
        if st.button('Convert to Sketch'):
            with st.spinner('Converting to Sketch...'):
                try:
                    img.save("uploaded_image.jpg")  # Save the uploaded file as a jpg
                    sketch = gfg.sketch_from_image("uploaded_image.jpg")
                    sketch.draw(threshold=100)
                    st.image("sketch.jpg", caption='Sketch Image.', use_column_width=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
