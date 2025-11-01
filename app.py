import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from gtts import gTTS

# --- PAGE CONFIG ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻️", layout="centered")

# --- MODERN STYLING ---
st.markdown("""
<style>
/* Background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    color: #76ff03;
    text-shadow: 0px 0px 25px #76ff03, 0px 0px 40px #00e676;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    font-style: italic;
    color: #b9f6ca;
    margin-bottom: 20px;
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #76ff03 !important;
    border-radius: 15px;
    background-color: rgba(255,255,255,0.05);
}

/* Uploaded image */
img {
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(118, 255, 3, 0.4);
}

/* Result card */
.result-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0,255,127,0.3);
    margin-top: 20px;
    animation: fadeIn 1s ease-in-out;
}

/* Prediction text */
.predicted {
    font-size: 30px;
    font-weight: bold;
    color: #76ff03;
    text-shadow: 0 0 20px #00e676;
}

/* Confidence */
.confidence {
    font-size: 20px;
    color: #b2ff59;
}

/* Tip text */
.tip {
    font-size: 18px;
    color: #e8f5e9;
    margin-top: 15px;
}

/* Voice button */
.voice-button {
    display: flex;
    justify-content: center;
    margin-top: 15px;
}

.voice-button button {
    background: linear-gradient(90deg, #76ff03, #00e676);
    color: black;
    border-radius: 50px;
    height: 50px;
    width: 200px;
    border: none;
    font-size: 17px;
    font-weight: bold;
    animation: pulse 2s infinite;
    cursor: pointer;
}

.voice-button button:hover {
    transform: scale(1.08);
}

/* Footer */
.footer {
    text-align: center;
    color: #c8e6c9;
    margin-top: 40px;
    font-size: 16px;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(118, 255, 3, 0.7); }
  70% { box-shadow: 0 0 0 20px rgba(118, 255, 3, 0); }
  100% { box-shadow: 0 0 0 0 rgba(118, 255, 3, 0); }
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="title">♻️ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a waste image — let AI classify and suggest how to keep the place clean 🌿</p>', unsafe_allow_html=True)

# --- LOAD MODEL ---
model = tf.keras.models.load_model("model/EcoSortAI_model.h5")

class_names = ['metal', 'organic', 'paper', 'plastic']
eco_tips = {
    "metal": "🪙 Collect and sell metal waste to recyclers — avoid mixing with general trash.",
    "organic": "🍃 Compost organic waste into nutrient-rich soil. Great for gardening!",
    "paper": "📄 Reuse or recycle paper. Avoid burning — it releases harmful gases.",
    "plastic": "🧴 Drop off plastic at recycling centers. Avoid single-use plastics."
}

uploaded_file = st.file_uploader("📸 Upload Waste Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_container_width=True)

    img = image.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    st.markdown("🔍 **Analyzing with AI...**")
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions) * 100)

    # --- RESULT CARD ---
    st.markdown(f"""
        <div class="result-card">
            <p class="predicted">✅ {predicted_class.upper()}</p>
            <p class="confidence">Confidence: {confidence:.2f}%</p>
            <p class="tip">{eco_tips[predicted_class]}</p>
        </div>
    """, unsafe_allow_html=True)

    # --- VOICE ASSISTANT ---
    tts = gTTS(text=f"This is {predicted_class}. {eco_tips[predicted_class]}", lang='en')
    audio_path = "eco_tip.mp3"
    tts.save(audio_path)
    audio_file = open(audio_path, "rb").read()

    st.markdown('<div class="voice-button"><button>🎧 Listen to Eco Tip</button></div>', unsafe_allow_html=True)
    st.audio(audio_file, format="audio/mp3")

# --- FOOTER ---
st.markdown("""
<div class="footer">
Developed by <b>Kavibharathi S</b> | AICTE–Shell–Edunet Green Skills Internship 🌍<br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
