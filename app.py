# app.py — EcoSort AI (Optimized: faster prediction + optional GPU support)
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import tempfile
import os
import time
from huggingface_hub import hf_hub_download

# Try offline TTS (pyttsx3). If not available, audio will be skipped gracefully.
try:
    import pyttsx3
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# -----------------------
# ORIGINAL UI STYLING (unchanged)
# -----------------------
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
.voice-button {display:flex; justify-content:center; margin-top:15px;}
.voice-button button {background:linear-gradient(90deg,#76ff03,#00e676); color:black; border-radius:50px; height:50px; width:200px; border:none; font-size:17px; font-weight:bold; cursor:pointer;}
.footer {text-align:center; color:#c8e6c9; margin-top:40px; font-size:16px;}
</style>
""", unsafe_allow_html=True)

# -----------------------
# TITLE
# -----------------------
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste in real-time 🌿</p>', unsafe_allow_html=True)

# -----------------------
# SETTINGS / PERFORMANCE TWEAKS
# -----------------------
# Use a smaller input size for faster inference (adjust if your model expects a different shape)
INPUT_SIZE = (128, 128)  # reduced from 150 -> faster

# small sleep time in camera loop to reduce CPU (seconds)
CAMERA_LOOP_SLEEP = 0.02

# -----------------------
# TTS: initialize engine once (cached)
# -----------------------
@st.cache_resource
def init_tts_engine():
    if not TTS_AVAILABLE:
        return None
    try:
        engine = pyttsx3.init()
        # Optional: set voice properties for speed or volume here
        engine.setProperty('rate', 150)   # speaking rate (words per minute)
        engine.setProperty('volume', 1.0) # 0.0 to 1.0
        return engine
    except Exception:
        return None

tts_engine = init_tts_engine()

def speak_text_offline(text: str):
    """Generate audio with pyttsx3 and return temp filename; safe no-op if TTS unavailable."""
    if tts_engine is None:
        return None
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tmp_name = tmp.name
        tmp.close()
        # pyttsx3 save_to_file + runAndWait
        engine = tts_engine
        engine.save_to_file(text, tmp_name)
        engine.runAndWait()
        return tmp_name
    except Exception:
        return None

# -----------------------
# MODEL LOADING (cached + optional GPU)
# -----------------------
@st.cache_resource
def load_model_from_hf():
    """
    Downloads model from HuggingFace (cached) and loads it.
    Uses tf.device('/GPU:0') if available, otherwise CPU.
    """
    try:
        # download model file from repo (filename path inside repo)
        model_file = hf_hub_download(repo_id="kavi11662/ecosort-ai", filename="model/EcoSortAI_model.h5")
    except Exception as e:
        # If hf_hub_download fails, propagate so UI can show error
        raise RuntimeError(f"HuggingFace download failed: {e}")

    # Try to use GPU if available
    try:
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            # allow memory growth to be friendlier on shared hosts
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            device = '/GPU:0'
        else:
            device = '/CPU:0'
    except Exception:
        device = '/CPU:0'

    # Load model inside device context if possible
    try:
        with tf.device(device):
            model = tf.keras.models.load_model(model_file)
    except Exception:
        # fallback to normal load
        model = tf.keras.models.load_model(model_file)

    return model

# load model (cached)
try:
    model = load_model_from_hf()
    model_loaded = True
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None
    model_loaded = False

# -----------------------
# Helper functions
# -----------------------
class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Collect and sell metal waste to recyclers — avoid mixing with general trash.",
    "organic": "🍃 Compost organic waste into nutrient-rich soil. Great for gardening!",
    "paper": "📄 Reuse or recycle paper. Avoid burning — it releases harmful gases.",
    "plastic": "🧴 Drop off plastic at recycling centers. Avoid single-use plastics."
}

def preprocess_pil(image_pil):
    """Fast preprocess using OpenCV where possible. Returns shape (1, H, W, C)."""
    # convert PIL -> numpy RGB
    img = np.array(image_pil.convert('RGB'))
    img = cv2.resize(img, INPUT_SIZE, interpolation=cv2.INTER_AREA)
    img = img.astype('float32') / 255.0
    return np.expand_dims(img, axis=0)

def preprocess_cv2_frame(frame_bgr):
    """Frame comes from cv2 (BGR). Resize and convert to RGB normalized array."""
    img = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, INPUT_SIZE, interpolation=cv2.INTER_AREA)
    img = img.astype('float32') / 255.0
    return np.expand_dims(img, axis=0)

# Optional: wrap model.predict in tf.function for slight speedup if supported
try:
    # create a small callable for inference that may be accelerated
    @tf.function
    def fast_predict(x):
        return model(x, training=False)
    HAVE_TF_FUNCTION = True
except Exception:
    fast_predict = None
    HAVE_TF_FUNCTION = False

def predict_input(input_array):
    """Predict with safe fallback. input_array shape (1,H,W,C)."""
    if model is None:
        return None
    try:
        if HAVE_TF_FUNCTION and fast_predict is not None:
            preds = fast_predict(tf.constant(input_array))
            preds = preds.numpy()
        else:
            preds = model.predict(input_array)
        return preds
    except Exception:
        # fallback to eager predict
        return model.predict(input_array)

# -----------------------
# INPUT METHOD
# -----------------------
option = st.selectbox("Select input method:", ["Upload Image", "Live Camera Feed"])

# -----------------------
# UPLOAD IMAGE SECTION
# -----------------------
if option == "Upload Image" and model_loaded:
    uploaded_file = st.file_uploader("📸 Upload Waste Image", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
        except Exception as e:
            st.error(f"Cannot open image: {e}")
            image = None

        if image is not None:
            st.image(image, caption="📷 Uploaded Image", use_container_width=True)

            # preprocess
            input_arr = preprocess_pil(image)

            # predict
            with st.spinner("Classifying... ♻"):
                preds = predict_input(input_arr)
                if preds is None:
                    st.error("Model not available for prediction.")
                else:
                    idx = int(np.argmax(preds))
                    predicted_class = class_names[idx]
                    confidence = float(np.max(preds) * 100)

                    st.markdown(f"""
                    <div class="result-card">
                        <p class="predicted">✅ {predicted_class.upper()}</p>
                        <p class="confidence">Confidence: {confidence:.2f}%</p>
                        <p class="tip">{eco_tips[predicted_class]}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    # Offline TTS (safe)
                    tts_text = f"This is {predicted_class}. {eco_tips[predicted_class]}"
                    audio_file = speak_text_file = None
                    if TTS_AVAILABLE:
                        audio_file = speak_text_offline(tts_text)
                    if audio_file:
                        try:
                            st.audio(audio_file, format="audio/mp3")
                        except Exception:
                            pass

# -----------------------
# LIVE CAMERA SECTION
# -----------------------
elif option == "Live Camera Feed" and model_loaded:
    st.markdown("📷 Live waste detection active — click Start Camera to classify!")

    if 'camera_running' not in st.session_state:
        st.session_state.camera_running = False

    col1, col2 = st.columns(2)
    with col1:
        start_cam = st.button("Start Camera")
    with col2:
        stop_cam = st.button("Stop Camera")

    FRAME_WINDOW = st.empty()
    RESULT_WINDOW = st.empty()

    if start_cam:
        st.session_state.camera_running = True
    if stop_cam:
        st.session_state.camera_running = False
        st.success("Camera stopped.")
        FRAME_WINDOW.empty()
        RESULT_WINDOW.empty()

    if st.session_state.camera_running:
        # Try to open camera with a few indexes (0,1) for better compatibility
        cap = None
        for cam_idx in (0, 1, 2):
            cap = cv2.VideoCapture(cam_idx)
            if cap is None or not cap.isOpened():
                continue
            else:
                break
        if cap is None or not cap.isOpened():
            st.error("Could not open camera. Ensure camera permission is granted.")
        else:
            last_pred = ""
            try:
                while st.session_state.camera_running:
                    ret, frame = cap.read()
                    if not ret:
                        time.sleep(0.05)
                        continue

                    # fast display (convert BGR->RGB)
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FRAME_WINDOW.image(frame_rgb, channels="RGB")

                    # preprocess and predict
                    input_arr = preprocess_cv2_frame(frame)
                    preds = predict_input(input_arr)
                    if preds is None:
                        continue
                    idx = int(np.argmax(preds))
                    predicted_class = class_names[idx]
                    confidence = float(np.max(preds) * 100)

                    RESULT_WINDOW.markdown(f"""
                    <div class="result-card">
                        <p class="predicted">✅ {predicted_class.upper()}</p>
                        <p class="confidence">Confidence: {confidence:.2f}%</p>
                        <p class="tip">{eco_tips[predicted_class]}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    # speak only when prediction changes (reduce audio spam)
                    if predicted_class != last_pred:
                        if TTS_AVAILABLE:
                            tts_text = f"This is {predicted_class}. {eco_tips[predicted_class]}"
                            audio_file = speak_text_offline(tts_text)
                            if audio_file:
                                try:
                                    st.audio(audio_file, format="audio/mp3")
                                except Exception:
                                    pass
                        last_pred = predicted_class

                    # small sleep to reduce CPU usage
                    time.sleep(CAMERA_LOOP_SLEEP)

            finally:
                cap.release()

# -----------------------
# FOOTER
# -----------------------
st.markdown("""
<div class="footer">
Developed by <b>Kavibharathi S</b> | AICTE–Shell–Edunet Green Skills Internship 🌍<br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
