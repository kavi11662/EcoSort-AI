import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from gtts import gTTS
import base64
import io
import time
from huggingface_hub import hf_hub_download

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
        color: white;
    }
    [data-testid="stSidebar"] {
        background-color: #1e3c50;
    }
    h1, h2, h3, h4 { color: #00ffcc; }
    .css-1kyxreq { background-color: #0d1b2a !important; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# LOAD MODEL FROM HUGGINGFACE
# --------------------------------------------------------

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

# --------------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------------

def preprocess_image(image):
    img = image.resize((150, 150))  # Change based on your model input
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_data = fp.read()
    b64 = base64.b64encode(audio_data).decode()
    st.audio(audio_data, format="audio/mp3")

# --------------------------------------------------------
# UI TITLE
# --------------------------------------------------------

st.title("♻ EcoSort AI")
st.subheader("Choose image upload or live camera — AI will classify waste in real-time 🌿")

st.markdown("---")

# --------------------------------------------------------
# INPUT SELECTION
# --------------------------------------------------------

option = st.radio("Select input method:", ["Upload Image"])

# --------------------------------------------------------
# UPLOAD IMAGE
# --------------------------------------------------------

if option == "Upload Image":
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if file and model:
        image = Image.open(file).convert("RGB")
        st.image(image, caption="Uploaded Image", width=300)

        with st.spinner("Analyzing... ♻"):
            time.sleep(1)
            input_data = preprocess_image(image)
            prediction = model.predict(input_data)
            result_class = np.argmax(prediction)

            classes = ["Biodegradable Waste", "Non-Biodegradable Waste"]
            result_text = classes[result_class]

        st.success(f"**Prediction: {result_text}**")

        speak_text(f"This is {result_text}")

# --------------------------------------------------------
# FOOTER
# --------------------------------------------------------

st.markdown("---")
st.markdown("""
### Developed by **Kavibharathi S**  
AICTE–Shell–Edunet Green Skills Internship 🌍  
*"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"*
""")
