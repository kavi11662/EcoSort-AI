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
[data-testid="stFileUploader"] {border:2px dashed #76ff03 !important; border-radius:15px;}
.result-card {background:rgba(255,255,255,0.08); padding:30px; border-radius:20px; text-align:center;}
.predicted {font-size:30px; font-weight:bold; color:#76ff03;}
.confidence {font-size:20px; color:#b2ff59;}
.tip {font-size:18px; color:#e8f5e9;}
.footer {text-align:center; color:#c8e6c9; margin-top:40px;}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste 🌿</p>', unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="kavi11662/ecosort-ai",
        filename="model/EcoSortAI_model.h5"
    )
    return tf.keras.models.load_model(model_path)

try:
    model = load_model()
    model_loaded = True
except:
    st.error("❌ Could not load model")
    model_loaded = False

class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Recycle metal waste separately.",
    "organic": "🍃 Compost organic waste.",
    "paper": "📄 Reuse or recycle paper.",
    "plastic": "🧴 Avoid single-use plastics."
}

# -------------------------
# SESSION FLAGS
# -------------------------
if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

option = st.selectbox("Choose method:", ["Upload Image", "Live Camera Feed"])

# -------------------------
# UPLOAD IMAGE
# -------------------------
if option == "Upload Image" and model_loaded:
    file = st.file_uploader("📸 Upload Image", type=["jpg","jpeg","png"])
    if file:
        image = Image.open(file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img = np.array(image.resize((150,150))) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img)
        cls = class_names[np.argmax(pred)]
        conf = float(np.max(pred) * 100)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">✅ {cls.upper()}</p>
            <p class="confidence">Confidence: {conf:.2f}%</p>
            <p class="tip">{eco_tips[cls]}</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# LIVE CAMERA (SAFE VERSION)
# -------------------------
elif option == "Live Camera Feed" and model_loaded:

    st.markdown("### 📷 Live Waste Detection")

    col1, col2 = st.columns(2)
    start = col1.button("▶ START CAMERA")
    stop = col2.button("⛔ STOP CAMERA")

    if start:
        st.session_state.camera_on = True

    if stop:
        st.session_state.camera_on = False

    if st.session_state.camera_on:
        img_file = st.camera_input("Capture Live Frame")

        if img_file:
            image = Image.open(img_file)
            st.image(image, caption="Live Frame", use_container_width=True)

            img = np.array(image.resize((150,150))) / 255.0
            img = np.expand_dims(img, axis=0)

            pred = model.predict(img)
            cls = class_names[np.argmax(pred)]
            conf = float(np.max(pred) * 100)

            st.markdown(f"""
            <div class="result-card">
                <p class="predicted">✅ {cls.upper()}</p>
                <p class="confidence">Confidence: {conf:.2f}%</p>
                <p class="tip">{eco_tips[cls]}</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
Developed by <b>Kavibharathi S</b> | AICTE–Shell–Edunet–Shell Green Skills Internship 🌍<br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
