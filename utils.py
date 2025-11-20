import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download

def global_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
        color: white;
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

@st.cache_resource
def load_model():
    try:
        path = hf_hub_download(
            repo_id="kavi11662/ecosort-ai",
            filename="model/EcoSort_model.h5"
        )
        return tf.keras.models.load_model(path)
    except Exception as e:
        st.error(f"Model Load Error: {e}")
        return None

CLASS_NAMES = [
    'battery', 'biological', 'cardboard', 'clothes', 'glass',
    'metal', 'paper', 'plastic', 'shoes', 'trash'
]

ECO_TIPS = {
    "battery": "Dispose batteries at authorized e-waste centers.",
    "biological": "Compost biodegradable waste safely.",
    "cardboard": "Flatten and recycle cardboard boxes.",
    "clothes": "Donate or recycle old clothes.",
    "glass": "Recycle separated glass responsibly.",
    "metal": "Metal is valuable — recycle it.",
    "paper": "Reuse or recycle clean paper.",
    "plastic": "Clean and recycle plastic waste.",
    "shoes": "Donate usable shoes or recycle.",
    "trash": "Dispose general waste responsibly."
}

def classify_image(image, model):
    img = np.array(image.resize((150,150))) / 255.0
    img = np.expand_dims(img, 0)
    preds = model.predict(img)
    class_id = int(np.argmax(preds))
    return CLASS_NAMES[class_id], float(np.max(preds)*100), ECO_TIPS[CLASS_NAMES[class_id]]
