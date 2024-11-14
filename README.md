```markdown
# 🎨 Sketch Magician

Transform your photos into stunning pencil sketches with **Sketch Magician**, a web app built using Streamlit and OpenCV. This tool lets you adjust the sketch style by modifying the blur intensity and download the final sketch. Ideal for artists, photographers, and anyone looking to experiment with creative effects!

## 🚀 Demo
Check out the deployed app: [Sketch Magician on Streamlit](https://your-streamlit-app-link)

## 📸 App Preview
![App Screenshot](path/to/screenshot.png)

## 📋 Features
- **Image Upload:** Upload any JPEG or PNG image.
- **Adjustable Sketch Intensity:** Modify the blur intensity to control sketch detail.
- **Download Option:** Easily download the final sketch image.
- **Responsive Design:** Optimized for desktops and mobile devices.
- **Footer with Social Links:** Connect with the developer on LinkedIn, GitHub, and more.

## 🛠️ How It Works
1. **Convert to Grayscale:** The image is converted to grayscale.
2. **Inversion and Blurring:** The grayscale image is inverted and blurred to create a base for sketching.
3. **Division for Sketch Effect:** The original grayscale image is divided by the blurred image, resulting in a sketch effect.

## 🎬 Quick Start
Follow these steps to run Sketch Magician locally on your machine.

### Prerequisites
- **Python 3.8+**
- **Streamlit**
- **OpenCV**
- **NumPy**
- **Pillow**

Install dependencies by running:
```
pip install streamlit opencv-python-headless numpy pillow
```

### Running the App
1. **Clone the repository and navigate to the project directory:**
   ```
   git clone https://github.com/your-username/sketch-magician.git
   cd sketch-magician
   ```

2. **Start the Streamlit app:**
   ```
   streamlit run app.py
   ```

3. **Visit** `http://localhost:8501` **in your browser to access the app.**

## 📄 Code Overview
- **`app.py`**: The main Streamlit app file, containing the UI and sketch conversion logic.
- **`convert_to_sketch()`**: Core function for creating the sketch effect using OpenCV.
- **`footer()`**: Function to render the footer with social media links.

## 📝 Usage
1. **Upload an image** in `.jpg` or `.png` format.
2. **Adjust the Blur Intensity** slider to modify the sketch style.
3. **Download the resulting sketch** with a single click.

## 🧑‍💻 Developer Info

**Developed by**: Gandham Mani Saketh  
**LinkedIn**: [Gandham Mani Saketh](https://www.linkedin.com/in/gandhammanisaketh2421/)  
**GitHub**: [GANDHAMMANI](https://github.com/GANDHAMMANI)  
**Instagram**: [mr.pandapal](https://www.instagram.com/mr.pandapal/)  

## 🤝 Contributing
Pull requests are welcome! If you have ideas for improving the app, please feel free to contribute. For major changes, open an issue to discuss your ideas.

## 📝 License
This project is licensed under the MIT License.

---

**Thank you for checking out Sketch Magician!** ✨
```