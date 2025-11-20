import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download


# -----------------------------
#  GLOBAL CSS (UI Styling)
# -----------------------------
def global_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .navbar {
        display: flex;
        justify-content: center;
        gap: 40px;
        background: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        backdrop-filter: blur(4px);
    }
    .nav-item {
        color: #76ff03;
        font-size: 20px;
        font-weight: 600;
        text-decoration: none;
    }
    .nav-item:hover {
        color: #00e676;
    }
    .title {
        text-align:center; font-size:52px; font-weight:900;
        color:#76ff03;
        text-shadow:0 0 25px #76ff03, 0 0 40px #00e676;
    }
    .subtitle {
        text-align:center; font-size:18px; font-style:italic;
        color:#b9f6ca;
    }
    .result-card {
        background: rgba(255,255,255,0.08);
        padding: 30px;
        border-radius: 20px;
        margin-top: 25px;
        text-align: center;
    }
    .predicted { font-size:30px; color:#76ff03; font-weight:bold; }
    .confidence { font-size:20px; color:#b2ff59; }
    .tip { font-size:18px; color:#e8f5e9; margin-top:10px; }
    </style>
    """, unsafe_allow_html=True)


# -----------------------------
#  NAVIGATION MENU
# -----------------------------
def navbar():
    st.markdown("""
    <div class="navbar">
        <a class="nav-item" href="./Home" target="_self">Home</a>
        <a class="nav-item" href="./About" target="_self">About</a>
        <a class="nav-item" href="./Features" target="_self">Features</a>
        <a class="nav-item" href="./Classifier" target="_self">EcoSort AI</a>
        <a class="nav-item" href="./Contact" target="_self">Contact</a>
    </div>
    """, unsafe_allow_html=True)



# -----------------------------
#  LOAD MODEL FROM HUGGINGFACE
# -----------------------------
@st.cache_resource
def load_model():
    try:
        model_path = hf_hub_download(
            repo_id="kavi11662/ecosort-ai",
            filename="model/EcoSort_model.h5"
        )
        return tf.keras.models.load_model(model_path)

    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None


# -----------------------------
#  CLASS LABELS
# -----------------------------
CLASS_NAMES = [
    'battery', 'biological', 'cardboard', 'clothes', 'glass',
    'metal', 'paper', 'plastic', 'shoes', 'trash'
]

# -----------------------------
#  ECO TIPS
# -----------------------------
ECO_TIPS = {
    "battery": "Batteries contain harmful chemicals. Dispose only at e-waste collection centers.",
    "biological": "Biological waste should be composted or handled safely.",
    "cardboard": "Flatten cardboard boxes and send them to recycling centers.",
    "clothes": "Donate usable clothes. Recycle torn clothes into cleaning cloths.",
    "glass": "Separate glass by color and recycle.",
    "metal": "Metal can be sold to scrap dealers — highly recyclable.",
    "paper": "Recycle paper or reuse it. Keep it dry.",
    "plastic": "Avoid single-use plastics. Clean and recycle.",
    "shoes": "Donate usable shoes. Recycle damaged ones.",
    "trash": "Dispose general waste responsibly. Avoid mixing recyclables into it."
}


# -----------------------------
#  CLASSIFY IMAGE
# -----------------------------
def classify_image(image, model):
    img_array = np.array(image.resize((150, 150))) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    class_id = int(np.argmax(preds))
    class_name = CLASS_NAMES[class_id]
    conf = float(np.max(preds) * 100)

    return class_name, conf, ECO_TIPS[class_name]
