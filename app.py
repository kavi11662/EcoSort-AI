import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download

# --- PAGE CONFIG ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# --- UI STYLING ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364); color: white;}
.title {text-align:center; font-size:52px; font-weight:900; color:#76ff03; text-shadow:0px 0px 25px #76ff03,0px 0px 40px #00e676;}
.subtitle {text-align:center; font-size:18px; font-style:italic; color:#b9f6ca;}
.result-card {background:rgba(255,255,255,0.08); padding:25px; border-radius:20px; text-align:center;}
.predicted {font-size:30px; font-weight:bold; color:#76ff03;}
.confidence {font-size:20px; color:#b2ff59;}
.tip {font-size:18px; color:#e8f5e9;}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste in real-time 🌿</p>', unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    path = hf_hub_download(
        repo_id="kavi11662/ecosort-ai",
        filename="model/EcoSortAI_model.h5"
    )
    return tf.keras.models.load_model(path)

model = load_model()
class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Collect and sell metal waste to recyclers.",
    "organic": "🍃 Compost organic waste — great for plants!",
    "paper": "📄 Reuse or recycle paper instead of burning.",
    "plastic": "🧴 Reduce single-use plastics — recycle properly."
}

# --- PREDICT FUNCTION ---
def predict_image(image):
    img = image.resize((150, 150))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, 0)
    preds = model.predict(img)
    cls = class_names[np.argmax(preds)]
    conf = float(np.max(preds) * 100)
    return cls, conf

# --- INPUT OPTION ---
option = st.selectbox("Select input method:", ["Upload Image", "Live Camera Feed"])

# --- IMAGE UPLOAD ---
if option == "Upload Image":
    uploaded = st.file_uploader("📸 Upload Waste Image", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image", use_container_width=True)

        cls, conf = predict_image(img)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">✅ {cls.upper()}</p>
            <p class="confidence">Confidence: {conf:.2f}%</p>
            <p class="tip">{eco_tips[cls]}</p>
        </div>
        """, unsafe_allow_html=True)

# --- LIVE CAMERA FEED WITH START/STOP BUTTONS ---
elif option == "Live Camera Feed":

    if "show_cam" not in st.session_state:
        st.session_state.show_cam = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶ Start Camera"):
            st.session_state.show_cam = True
    with col2:
        if st.button("⏹ Stop Camera"):
            st.session_state.show_cam = False

    if st.session_state.show_cam:
        st.markdown("📷 Take a live picture to classify the waste")
        camera_image = st.camera_input("Live Camera")

        if camera_image:
            img = Image.open(camera_image)
            st.image(img, caption="Captured Image", use_container_width=True)

            cls, conf = predict_image(img)

            st.markdown(f"""
            <div class="result-card">
                <p class="predicted">✅ {cls.upper()}</p>
                <p class="confidence">Confidence: {conf:.2f}%</p>
                <p class="tip">{eco_tips[cls]}</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; margin-top:30px; color:#b2ff59;">
Developed by <b>Kavibharathi S</b> 🌱 | AICTE–Shell–Edunet Internship
</div>
""", unsafe_allow_html=True)
