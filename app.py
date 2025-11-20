# import streamlit as st
# import tensorflow as tf
# import numpy as np
# from PIL import Image
# from huggingface_hub import hf_hub_download

# # --- PAGE CONFIG ---
# st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# # --- ORIGINAL UI STYLING ---
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] {background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364); color: white;}
# .title {text-align:center; font-size:52px; font-weight:900; color:#76ff03; text-shadow:0px 0px 25px #76ff03,0px 0px 40px #00e676; margin-bottom:5px;}
# .subtitle {text-align:center; font-size:18px; font-style:italic; color:#b9f6ca; margin-bottom:20px;}
# [data-testid="stFileUploader"] {border:2px dashed #76ff03 !important; border-radius:15px; background-color:rgba(255,255,255,0.05);}
# img {border-radius:20px; box-shadow:0 0 25px rgba(118,255,3,0.4);}
# .result-card {background:rgba(255,255,255,0.08); border-radius:20px; padding:30px; text-align:center; box-shadow:0 0 25px rgba(0,255,127,0.3); margin-top:20px;}
# .predicted {font-size:30px; font-weight:bold; color:#76ff03; text-shadow:0 0 20px #00e676;}
# .confidence {font-size:20px; color:#b2ff59;}
# .tip {font-size:18px; color:#e8f5e9; margin-top:15px;}
# .footer {text-align:center; color:#c8e6c9; margin-top:40px; font-size:16px;}
# </style>
# """, unsafe_allow_html=True)

# # --- TITLE ---
# st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
# st.markdown('<p class="subtitle">Choose image upload or live camera — AI will classify waste in real-time 🌿</p>', unsafe_allow_html=True)

# # --- LOAD MODEL FROM HUGGINGFACE ---
# @st.cache_resource
# def load_model():
#     try:
#         model_path = hf_hub_download(
#             repo_id="kavi11662/ecosort-ai",
#             filename="model/EcoSort_model.h5"  # EXACT FILE NAME
#         )
#         model = tf.keras.models.load_model(model_path)
#         return model
#     except Exception as e:
#         st.error(f"Error loading model: {e}")
#         return None

# model = load_model()
# model_loaded = model is not None

# # --- 10 NEW CLASSES ---
# class_names = [
#     'battery', 'biological', 'cardboard', 'clothes', 'glass',
#     'metal', 'paper', 'plastic', 'shoes', 'trash'
# ]

# # TIPS FOR EACH CLASS
# eco_tips = {
#     "battery": "Batteries contain harmful chemicals. Dispose only at e-waste collection centers.",
#     "biological": "Biological waste should be composted or handled safely if hazardous.",
#     "cardboard": "Flatten cardboard boxes and send them to recycling centers.",
#     "clothes": "Donate usable clothes. Recycle torn clothes into cleaning cloths.",
#     "glass": "Separate glass by color and recycle. Handle broken glass carefully.",
#     "metal": "Metal can be sold to scrap dealers — highly recyclable.",
#     "paper": "Recycle paper or reuse for crafts. Keep it dry for best quality.",
#     "plastic": "Avoid single-use plastics. Clean and send for recycling.",
#     "shoes": "Donate usable shoes. Recycle damaged ones at textile centers.",
#     "trash": "General waste — avoid mixing recyclable items with it."
# }

# # --- INPUT METHOD ---
# option = st.selectbox("Select input method:", ["Upload Image", "Live Camera Feed"])

# # UPLOAD IMAGE
# if option == "Upload Image" and model_loaded:
#     uploaded_file = st.file_uploader("📸 Upload Waste Image", type=["jpg","jpeg","png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="📷 Uploaded Image", use_container_width=True)

#         img_array = np.array(image.resize((150,150))) / 255.0
#         img_array = np.expand_dims(img_array, axis=0)

#         predictions = model.predict(img_array)
#         predicted_class = class_names[np.argmax(predictions)]
#         confidence = float(np.max(predictions) * 100)

#         st.markdown(f"""
#         <div class="result-card">
#             <p class="predicted">✅ {predicted_class.upper()}</p>
#             <p class="confidence">Confidence: {confidence:.2f}%</p>
#             <p class="tip">{eco_tips[predicted_class]}</p>
#         </div>
#         """, unsafe_allow_html=True)

# # LIVE CAMERA
# elif option == "Live Camera Feed" and model_loaded:
#     st.markdown("📷 Take a live picture to classify the waste")

#     img_file = st.camera_input("Open Camera")

#     if img_file:
#         image = Image.open(img_file)
#         st.image(image, caption="Captured Image", use_container_width=True)

#         img_array = np.array(image.resize((150,150))) / 255.0
#         img_array = np.expand_dims(img_array, axis=0)

#         predictions = model.predict(img_array)
#         predicted_class = class_names[np.argmax(predictions)]
#         confidence = float(np.max(predictions) * 100)

#         st.markdown(f"""
#         <div class="result-card">
#             <p class="predicted">✅ {predicted_class.upper()}</p>
#             <p class="confidence">Confidence: {confidence:.2f}%</p>
#             <p class="tip">{eco_tips[predicted_class]}</p>
#         </div>
#         """, unsafe_allow_html=True)

# # FOOTER
# st.markdown("""
# <div class="footer">
# Developed by <b>Kavibharathi S</b> <br>
# "Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
# </div>
# """, unsafe_allow_html=True)


import streamlit as st
from utils import global_css

# --- PAGE SETTINGS ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# --- APPLY GLOBAL STYLING ---
global_css()

# --- HERO SECTION ---
st.markdown("""
<div style="text-align:center; margin-top:50px; padding-bottom:20px;">
    <h1 class="title" style="margin-bottom:10px;">♻ EcoSort AI</h1>
    <p class="subtitle" style="font-size:20px; color:#c8f7d4;">
        Smart Waste Classification for a Cleaner Planet 🌿
    </p>
</div>
""", unsafe_allow_html=True)


# --- PROFESSIONAL FEATURE / HERO CONTENT ---
st.markdown("""
<div style="
    background: rgba(255,255,255,0.07);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,255,127,0.15);
    margin-top: 30px;
    text-align: center;
">

    <h2 style="color:#76ff03; margin-bottom:15px; font-size:32px;">
        Your Smart Waste Assistant
    </h2>

    <p style="font-size:18px; color:#e8f5e9; line-height:1.6; max-width:700px; margin:auto;">
        Simply upload or capture a picture of your waste —  
        <b>EcoSort AI instantly identifies the waste type</b>  
        and provides <b>eco-friendly recycling and disposal tips</b>  
        to help you contribute to a greener environment.
    </p>

</div>
""", unsafe_allow_html=True)


# --- BUTTON SECTION ---
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    clicked = st.button(
        "🚀 Try the Classifier",
        use_container_width=True,
        type="primary",
        help="Open the AI Waste Classifier"
    )

if clicked:
    st.switch_page("pages/3_Classifier.py")


# --- FOOTER ---
st.markdown("""
<br><br>
<div style="text-align:center; color:#d0ffd6; font-size:15px; opacity:0.9;">
Developed by <b>Kavibharathi S</b> • AICTE–Shell–Edunet Internship  
<br>
<span style="font-size:14px;">“Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱”</span>
</div>
""", unsafe_allow_html=True)











