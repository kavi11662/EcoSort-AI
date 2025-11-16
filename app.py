import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# --- ORIGINAL UI STYLING ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364); color: white;}
.title {text-align:center; font-size:52px; font-weight:900; color:#76ff03; text-shadow:0px 0px 25px #76ff03,0px 0px 40px #00e676; margin-bottom:5px;}
.subtitle {text-align:center; font-size:18px; font-style:italic; color:#b9f6ca; margin-bottom:20px;}
[data-testid="stFileUploader"] {border:2px dashed #76ff03 !important; border-radius:15px; background-color:rgba(255,255,255,0.05);}
img {border-radius:20px; box-shadow:0 0 25px rgba(118,255,3,0.4);}
.result-card {background:rgba(255,255,255,0.08); border-radius:20px; padding:30px; text-align:center; box-shadow:0 0 25px rgba(0,255,127,0.3); margin-top:20px;}
.predicted {font-size:30px; font-weight:bold; color:#76ff03; text-shadow:0 0 20px #00e676;}
.confidence {font-size:20px; color:#b2ff59;}
.tip {font-size:18px; color:#e8f5e9; margin-top:15px;}
.footer {text-align:center; color:#c8e6c9; margin-top:40px; font-size:16px;}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste in real-time 🌿</p>', unsafe_allow_html=True)

# --- LOAD MODEL FROM HUGGINGFACE ---
@st.cache_resource
def load_model():
    try:
        model_path = hf_hub_download(
            repo_id="kavi11662/ecosort-ai",
            filename="model/EcoSortAI_model.h5"
        )
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()
model_loaded = model is not None

class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Collect and sell metal waste to recyclers — avoid mixing with general trash.",
    "organic": "🍃 Compost organic waste into nutrient-rich soil. Great for gardening!",
    "paper": "📄 Reuse or recycle paper. Avoid burning — it releases harmful gases.",
    "plastic": "🧴 Drop off plastic at recycling centers. Avoid single-use plastics."
}

# SESSION STATE for live camera
if "camera_active" not in st.session_state:
    st.session_state.camera_active = False

# --- INPUT METHOD ---
option = st.selectbox("Select input method:", ["Upload Image", "Live Camera Feed"])

# --------------------------------------------------------------------
#  UPLOAD IMAGE
# --------------------------------------------------------------------
if option == "Upload Image" and model_loaded:
    uploaded_file = st.file_uploader("📸 Upload Waste Image", type=["jpg","jpeg","png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Image", use_container_width=True)

        img_array = np.array(image.resize((150,150))) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = float(np.max(predictions) * 100)

        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">✅ {predicted_class.upper()}</p>
            <p class="confidence">Confidence: {confidence:.2f}%</p>
            <p class="tip">{eco_tips[predicted_class]}</p>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------------------------
#  LIVE CAMERA FEED (START / STOP BUTTON VERSION)
# --------------------------------------------------------------------
elif option == "Live Camera Feed" and model_loaded:

    st.markdown("### 📷 Live Waste Detection")

    col1, col2 = st.columns(2)
    start = col1.button("▶ START CAMERA", type="primary")
    stop = col2.button("⛔ STOP CAMERA")

    if start:
        st.session_state.camera_active = True
        st.experimental_rerun()

    if stop:
        st.session_state.camera_active = False
        st.experimental_rerun()

    if st.session_state.camera_active:

        st.markdown("Camera is running...")

        img_file = st.camera_input("")

        if img_file:
            image = Image.open(img_file)
            st.image(image, caption="Live Frame", use_container_width=True)

            img_array = np.array(image.resize((150,150))) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            predictions = model.predict(img_array)
            predicted_class = class_names[np.argmax(predictions)]
            confidence = float(np.max(predictions) * 100)

            st.markdown(f"""
            <div class="result-card">
                <p class="predicted">✅ {predicted_class.upper()}</p>
                <p class="confidence">Confidence: {confidence:.2f}%</p>
                <p class="tip">{eco_tips[predicted_class]}</p>
            </div>
            """, unsafe_allow_html=True)

        # Auto-refresh every 1 second for live view
        time.sleep(1)
        st.experimental_rerun()

# --- FOOTER ---
st.markdown("""
<div class="footer">
Developed by <b>Kavibharathi S</b> | AICTE–Shell–Edunet Green Skills Internship 🌍<br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
