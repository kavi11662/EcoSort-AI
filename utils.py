import streamlit as st
import tensorflow as tf
import numpy as np
from huggingface_hub import hf_hub_download
from PIL import Image

@st.cache_resource
def load_model():
    try:
        model_path = hf_hub_download(
            repo_id="kavi11662/ecosort-ai",
            filename="model/EcoSort_model.h5"
        )
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

CLASS_NAMES = [
    'battery', 'biological', 'cardboard', 'clothes', 'glass',
    'metal', 'paper', 'plastic', 'shoes', 'trash'
]

ECO_TIPS = {
    "battery": "Dispose batteries only in certified e-waste bins.",
    "biological": "Biodegradable waste should be composted.",
    "cardboard": "Flatten & recycle cardboard boxes.",
    "clothes": "Donate reusable clothes, recycle torn ones.",
    "glass": "Recycle at glass centers. Handle broken glass carefully.",
    "metal": "Metal waste can be sold or recycled.",
    "paper": "Reuse or recycle clean paper.",
    "plastic": "Clean & recycle plastics to reduce pollution.",
    "shoes": "Donate wearable shoes, recycle damaged ones.",
    "trash": "General waste — avoid mixing recyclables."
}

def classify_image(model, image):
    img = image.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions) * 100)

    return predicted_class, confidence
