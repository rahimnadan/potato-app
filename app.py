
import streamlit as st
import requests
from PIL import Image
import io

# Constants
API_URL = "https://classify.roboflow.com"
API_KEY = "8WozafCyTLmGPySFcYCf"
MODEL_ID = "potato-blight-stage-detection/2"

def infer_image(image):
    """Send image to the model inference API and return the result."""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = buffered.getvalue()

    response = requests.post(
        f"{API_URL}/{MODEL_ID}",
        files={"file": img_str},
        params={"api_key": API_KEY}
    )

    return response.json()

# Streamlit app
st.set_page_config(page_title="Potato Leaf Disease Classification", page_icon=":leafy_green:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    .main-header {
        background-color: #4CAF50;
        padding: 10px;
        text-align: center;
        color: white;
    }
    .main-footer {
        background-color: #4CAF50;
        padding: 10px;
        text-align: center;
        color: white;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }
    .contact-info {
        margin-top: 10px;
        font-size: 14px;
    }
    .uploaded-image {
        border: 2px solid #4CAF50;
        margin: 10px 0;
        border-radius: 10px;
    }
    .prediction-result {
        background-color: #fff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    .file-upload-section {
        text-align: center;
        padding: 20px;
        border: 2px dashed #4CAF50;
        border-radius: 10px;
        background-color: #eafaf1;
        cursor: pointer;
    }
    .nav-tabs {
        background-color: #4CAF50;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .nav-tabs a {
        color: white;
        padding: 10px;
        text-decoration: none;
        margin: 0 5px;
    }
    .nav-tabs a.active {
        background-color: white;
        color: #4CAF50;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>Potato Leaf Disease Classification</h1>
    </div>
""", unsafe_allow_html=True)

# Navigation Tabs
tabs = ["Home", "Project Info", "About Us"]
active_tab = st.selectbox("", tabs, format_func=lambda x: x)

# Home Tab
if active_tab == "Home":
    st.markdown("""
        <div class="file-upload-section">
            <h3>Upload an Image of Potato Leaf</h3>
            <small>Select a potato leaf image to classify its disease</small>
        </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        if st.button('Predict'):
            st.write("Classifying...")

            result = infer_image(image)

            # Displaying the results in a better format
            st.markdown("<div class='prediction-result'><h3>Prediction Results:</h3>", unsafe_allow_html=True)
            if "predicted_classes" in result:
                for cls in result["predicted_classes"]:
                    confidence = result["predictions"][cls]["confidence"] * 100
                    st.markdown(f"<p>- <strong>{cls.replace('Potato___', '').replace('_', ' ')}:</strong> {confidence:.2f}%</p>", unsafe_allow_html=True)
            else:
                st.write("No prediction available.")
            st.markdown("</div>", unsafe_allow_html=True)

# Project Info Tab
elif active_tab == "Project Info":
    st.markdown("""
        <div>
            <h2>Project Information</h2>
            <h3>Introduction</h3>
            <p>This project focuses on the classification of potato leaf diseases using advanced machine learning techniques. Farmers and agricultural experts can benefit from this tool to quickly identify diseases and take appropriate actions to protect their crops.</p>
            <h3>Dataset</h3>
            <p>Plant Village</p>
            <h3>Technique Used</h3>
            <p>YOLOv5</p>
            <h3>Model Accuracy</h3>
            <p>98%</p>
            <h3>Deployment</h3>
            <p>Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

# About Us Tab
elif active_tab == "About Us":
    st.markdown("""
        <div>
            <h2>About Us</h2>
            <h3>Group Members</h3>
            <p>Abdur Rahim, Syed Umar</p>
            <h3>Supervisor</h3>
            <p>Dr. Sadaqat Jan</p>
            <h3>Department</h3>
            <p>CSE</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="main-footer">
        <p>Developed and Designed by Abdur Rahim & Syed Umar</p>
        <p class="contact-info">
            Contact: +92 3251556457 <br>
            <a href="https://www.linkedin.com/in/abdur-rahim-718ba4227" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" width="20px" style="vertical-align: middle;">
                LinkedIn
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)







