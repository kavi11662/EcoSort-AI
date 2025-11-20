import streamlit as st
from PIL import Image
from utils import global_css, load_model, classify_image

st.set_page_config(page_title="Classifier", page_icon="🧪")
global_css()

st.markdown('<h1 class="title">EcoSort AI Classifier</h1>', unsafe_allow_html=True)

model = load_model()

option = st.selectbox("Choose Input Type:", ["Upload Image", "Live Camera"])

if option == "Upload Image":
    file = st.file_uploader("Upload Waste Image", type=["jpg","jpeg","png"])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        cls, conf, tip = classify_image(img, model)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">{cls.upper()}</p>
            <p class="confidence">{conf:.2f}% confidence</p>
            <p class="tip">{tip}</p>
        </div>
        """, unsafe_allow_html=True)

else:
    cam = st.camera_input("Capture Image")
    if cam:
        img = Image.open(cam)
        st.image(img, use_container_width=True)
        cls, conf, tip = classify_image(img, model)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">{cls.upper()}</p>
            <p class="confidence">{conf:.2f}% confidence</p>
            <p class="tip">{tip}</p>
        </div>
        """, unsafe_allow_html=True)
