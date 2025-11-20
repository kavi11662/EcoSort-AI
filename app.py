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

st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="wide")
global_css()

# --- NAVBAR ---
st.markdown("""
<style>
.navbar {
    display:flex;
    justify-content:center;
    gap:35px;
    background:rgba(255,255,255,0.08);
    padding:15px;
    border-radius:12px;
    margin-bottom:40px;
}
.nav-item {
    color:#76ff03;
    font-size:20px;
    font-weight:600;
    text-decoration:none;
}
.nav-item:hover { color:#00e676; }
</style>

<div class="navbar">
    <a class="nav-item" href="/">Home</a>
    <a class="nav-item" href="/1_About">About</a>
    <a class="nav-item" href="/2_Features">Solution</a>
    <a class="nav-item" href="#">Blogs</a>
    <a class="nav-item" href="#">Survey</a>
    <a class="nav-item" href="/3_Classifier">Get Started</a>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<h1 style="text-align:center; color:#76ff03; font-size:55px; font-weight:900;">
From Waste to Wonder — Powered by Smart Technology
</h1>

<p style="text-align:center; font-size:20px; color:#e8f5e9; max-width:900px; margin:auto;">
EcoSortAI is a cleantech solution transforming how we sort waste.  
With intelligent automation and real-time insights, we help cities, homes, and businesses  
reduce landfill use, lower emissions, and move toward a zero-waste future.
</p>

<div style="text-align:center; margin-top:25px;">
    <a href="/3_Classifier">
        <button style="padding:15px 40px; font-size:20px; background:#76ff03; color:black; 
                       border:none; border-radius:10px; cursor:pointer;">
            Get Started 🚀
        </button>
    </a>

    <button style="padding:15px 40px; font-size:20px; background:transparent; color:#76ff03; 
                   border:2px solid #76ff03; border-radius:10px; margin-left:15px; cursor:pointer;">
        Join the Waitlist
    </button>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- WHY ECOSORT SECTION ----------------
st.markdown("""
<h2 style="color:#76ff03; font-size:40px; text-align:center;">Why EcoSortAI?</h2>

<p style="text-align:center; font-size:20px; color:#e8f5e9; max-width:850px; margin:auto;">
We built EcoSortAI to make sustainable living easy. With AI + smart sensors,  
our intelligent system automatically detects and sorts waste — no confusion, no mistakes.
</p>

<br>

<div style="display:flex; justify-content:center; gap:40px; flex-wrap:wrap;">

    <div style="width:300px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🌍 Sustainable Impact</h3>
        <p>Reduces landfill waste and promotes eco-friendly habits.</p>
    </div>

    <div style="width:300px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🌎 Global Readiness</h3>
        <p>Adapts to waste systems across regions worldwide.</p>
    </div>

    <div style="width:300px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🤖 Smart Technology</h3>
        <p>AI + ML ensure highly accurate waste sorting.</p>
    </div>

    <div style="width:300px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🔐 Secure & Reliable</h3>
        <p>Built with strong data privacy & robust performance.</p>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- HOW IT WORKS ----------------
st.markdown("""
<h2 style="color:#76ff03; font-size:40px; text-align:center;">How EcoSortAI Works</h2>
<br>

<div style="display:flex; justify-content:center; flex-wrap:wrap; gap:40px;">

    <div style="width:300px;">
        <h3 style="color:#76ff03;">1️⃣ Waste Detection</h3>
        <p>Smart sensors identify when waste is added.</p>
    </div>

    <div style="width:300px;">
        <h3 style="color:#76ff03;">2️⃣ AI Classification</h3>
        <p>Our ML model identifies the waste type instantly.</p>
    </div>

    <div style="width:300px;">
        <h3 style="color:#76ff03;">3️⃣ Automated Sorting</h3>
        <p>Robotic flaps place waste into the correct bin.</p>
    </div>

    <div style="width:300px;">
        <h3 style="color:#76ff03;">4️⃣ Real-Time Insights</h3>
        <p>Track your recycling performance and progress.</p>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- CHOOSE YOUR BIN ----------------
st.markdown("""
<h2 style="color:#76ff03; font-size:40px; text-align:center;">Choose Your EcoSortAI Bin</h2>
<br>

<div style="display:flex; justify-content:center; gap:50px; flex-wrap:wrap;">

    <div style="width:320px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🏡 Residential</h3>
        <p>Smart waste solution for homes and apartments.</p>
        <button style="margin-top:10px; padding:10px 20px; border:none; border-radius:8px; background:#76ff03;">
            Learn More
        </button>
    </div>

    <div style="width:320px; background:rgba(255,255,255,0.08); padding:25px; border-radius:15px;">
        <h3 style="color:#76ff03;">🏢 Corporate</h3>
        <p>Automated waste management for businesses.</p>
        <button style="margin-top:10px; padding:10px 20px; border:none; border-radius:8px; background:#76ff03;">
            Learn More
        </button>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<hr style="border:1px solid #76ff03;">

<p style="text-align:center; color:#b9f6ca;">
Made with 💚 by <b>Kavibharathi S</b> — AICTE Shell Edunet Green Skills Internship
</p>
""", unsafe_allow_html=True)














