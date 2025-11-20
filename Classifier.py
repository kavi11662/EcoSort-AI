import streamlit as st
from PIL import Image
from utils import navbar, global_css, load_model, classify_image

st.set_page_config(page_title="EcoSort Classifier", page_icon="♻")

global_css()
navbar()

st.markdown('<h1 class="title">EcoSort AI Classifier</h1>', unsafe_allow_html=True)

model = load_model()

option = st.selectbox("Choose Input Type:", ["Upload Image", "Live Camera Feed"])

# ------- Upload Image -------
if option == "Upload Image":
    file = st.file_uploader("Upload Waste Image", type=["jpg", "jpeg", "png"])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)

        cls, conf, tip = classify_image(img, model)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">{cls.upper()}</p>
            <p class="confidence">Confidence: {conf:.2f}%</p>
            <p class="tip">{tip}</p>
        </div>
        """, unsafe_allow_html=True)

# ------- Live Camera -------
elif option == "Live Camera Feed":
    cam = st.camera_input("Capture Image")
    if cam:
        img = Image.open(cam)
        st.image(img, use_container_width=True)

        cls, conf, tip = classify_image(image=img, model=model)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">{cls.upper()}</p>
            <p class="confidence">Confidence: {conf:.2f}%</p>
            <p class="tip">{tip}</p>
        </div>
        """, unsafe_allow_html=True)
