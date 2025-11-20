import streamlit as st
from PIL import Image
from utils import global_css, load_model, classify_image
import numpy as np

# Page config
st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻",
    layout="wide",
)

# Apply global CSS
global_css()

# Load model once
model = load_model()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Features", "Classifier", "Contact"]
)

# ---------------------------
# HOME PAGE
# ---------------------------
if page == "Home":
    st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Smart Waste Classification for a Cleaner Planet 🌿</p>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:40px;">
        <h2 style="color:#76ff03; margin-bottom:15px; font-size:32px;">
            Your Smart Waste Assistant
        </h2>
        <p style="font-size:18px; color:#e8f5e9; line-height:1.6; max-width:700px; margin:auto;">
            Simply upload or capture a picture of your waste —  
            <b>EcoSort AI instantly identifies the waste type</b>  
            and provides <b>eco-friendly recycling and disposal tips</b>  
            to help you contribute to a greener environment.
        </p>
        <br>
        <a href="#classifier">
            <button style="padding:15px 30px; font-size:20px; background:#76ff03;
                            border-radius:10px; border:none; cursor:pointer;">
                Try the Classifier 🚀
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### How EcoSort AI Works")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Waste Detection**")
        st.write("Smart sensors detect inserted waste.")
    with col2:
        st.markdown("**AI Classification**")
        st.write("Machine learning identifies waste type in real-time.")
    with col3:
        st.markdown("**Automated Sorting**")
        st.write("Directs waste into correct bins automatically.")
    with col4:
        st.markdown("**Real-Time Insights**")
        st.write("Track recycling progress instantly.")

# ---------------------------
# ABOUT PAGE
# ---------------------------
elif page == "About":
    st.markdown('<h1 class="title">About EcoSort AI</h1>', unsafe_allow_html=True)
    st.write("""
    EcoSort AI solves the real problem of improper waste segregation by using deep learning  
    to classify **10 types of waste** and provide correct disposal guidance.

    Its mission is to reduce pollution, support recycling, and promote clean surroundings.
    """)

# ---------------------------
# FEATURES PAGE
# ---------------------------
elif page == "Features":
    st.markdown('<h1 class="title">Features</h1>', unsafe_allow_html=True)
    st.write("""
    ### ✅ 10-Class Waste Detection  
    ### ✅ Upload Image or Live Camera  
    ### ✅ Instant Eco-Friendly Tips  
    ### ✅ HuggingFace Deep Learning Model  
    ### ✅ Clean Multi-Page UI  
    """)

# ---------------------------
# CLASSIFIER PAGE
# ---------------------------
elif page == "Classifier":
    st.markdown('<h1 class="title" id="classifier">EcoSort AI Classifier</h1>', unsafe_allow_html=True)

    option = st.selectbox("Choose Input Type:", ["Upload Image", "Live Camera"])

    # Upload
    if option == "Upload Image":
        file = st.file_uploader("Upload Waste Image", type=["jpg","jpeg","png"])
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
    else:
        cam = st.camera_input("Capture Image")
        if cam:
            img = Image.open(cam)
            st.image(img, use_container_width=True)
            cls, conf, tip = classify_image(img, model)
            st.markdown(f"""
            <div class="result-card">
                <p class="predicted">{cls.upper()}</p>
                <p class="confidence">Confidence: {conf:.2f}%</p>
                <p class="tip">{tip}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------
# CONTACT PAGE
# ---------------------------
elif page == "Contact":
    st.markdown('<h1 class="title">Contact</h1>', unsafe_allow_html=True)
    st.write("""
    ### Developer  
    **Kavibharathi S**

    ### Internship  
    AICTE – Shell – Edunet Green Skills Internship 🌍

    ### Project  
    EcoSort AI — Smart Waste Classification System
    """)
