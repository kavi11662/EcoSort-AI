 
import tensorflow as tf
import numpy as np
from PIL import Image
from gtts import gTTS
import cv2
import tempfile

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
.voice-button {display:flex; justify-content:center; margin-top:15px;}
.voice-button button {background:linear-gradient(90deg,#76ff03,#00e676); color:black; border-radius:50px; height:50px; width:200px; border:none; font-size:17px; font-weight:bold; cursor:pointer;}
.footer {text-align:center; color:#c8e6c9; margin-top:40px; font-size:16px;}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste in real-time 🌿</p>', unsafe_allow_html=True)

# --- LOAD MODEL ---
try:
    model = tf.keras.models.load_model("model/EcoSortAI_model.h5")
    model_loaded = True
except Exception as e:
    st.error(f"Error loading model: {e}")
    model_loaded = False

class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Collect and sell metal waste to recyclers — avoid mixing with general trash.",
    "organic": "🍃 Compost organic waste into nutrient-rich soil. Great for gardening!",
    "paper": "📄 Reuse or recycle paper. Avoid burning — it releases harmful gases.",
    "plastic": "🧴 Drop off plastic at recycling centers. Avoid single-use plastics."
}

# --- INPUT METHOD DROPDOWN ---
option = st.selectbox("Select input method:", ["Upload Image", "Live Camera Feed"])

# --- IMAGE UPLOAD ---
if option == "Upload Image" and model_loaded:
    uploaded_file = st.file_uploader("📸 Upload Waste Image", type=["jpg","jpeg","png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Image", use_container_width=True)
        img_array = np.array(image.resize((150,150)))/255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = float(np.max(predictions)*100)
        st.markdown(f"""
        <div class="result-card">
            <p class="predicted">✅ {predicted_class.upper()}</p>
            <p class="confidence">Confidence: {confidence:.2f}%</p>
            <p class="tip">{eco_tips[predicted_class]}</p>
        </div>
        """, unsafe_allow_html=True)
        tts = gTTS(text=f"This is {predicted_class}. {eco_tips[predicted_class]}", lang='en')
        audio_path = tempfile.NamedTemporaryFile(delete=False,suffix=".mp3").name
        tts.save(audio_path)
        st.audio(audio_path, format="audio/mp3")

# --- LIVE CAMERA FEED ---
elif option == "Live Camera Feed" and model_loaded:
    st.markdown("📷 Live waste detection active — click Start Camera to classify!")
    
    if 'camera_running' not in st.session_state:
        st.session_state.camera_running = False

    start_cam = st.button("Start Camera")
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
        cap = cv2.VideoCapture(0)
        last_pred = ""
        while st.session_state.camera_running:
            ret, frame = cap.read()
            if not ret:
                continue
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame_rgb, channels="RGB")
            img_pred = cv2.resize(frame,(150,150))/255.0
            img_pred = np.expand_dims(img_pred,axis=0)
            predictions = model.predict(img_pred)
            predicted_class = class_names[np.argmax(predictions)]
            confidence = float(np.max(predictions)*100)
            RESULT_WINDOW.markdown(f"""
            <div class="result-card">
                <p class="predicted">✅ {predicted_class.upper()}</p>
                <p class="confidence">Confidence: {confidence:.2f}%</p>
                <p class="tip">{eco_tips[predicted_class]}</p>
            </div>
            """, unsafe_allow_html=True)
            if predicted_class != last_pred:
                tts = gTTS(text=f"This is {predicted_class}. {eco_tips[predicted_class]}", lang='en')
                audio_path = tempfile.NamedTemporaryFile(delete=False,suffix=".mp3").name
                tts.save(audio_path)
                st.audio(audio_path, format="audio/mp3")
                last_pred = predicted_class
        cap.release()

# --- FOOTER ---
st.markdown("""
<div class="footer">
Developed by <b>Kavibharathi S</b> | AICTE–Shell–Edunet Green Skills Internship 🌍<br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
