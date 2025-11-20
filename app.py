
import streamlit as st
from utils import global_css

# --- PAGE SETTINGS ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# --- APPLY GLOBAL STYLING ---
global_css()

# --- TITLE & SUBTITLE ---
st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart Waste Classification for a Cleaner Planet 🌿</p>', unsafe_allow_html=True)

# --- HOME PAGE CONTENT ---
st.markdown("""
<div style="text-align:center; margin-top:40px;">
    <h2 style="color:#76ff03;">Your Smart Waste Assistant</h2>
    <p style="font-size:18px; color:#e8f5e9;">
        Capture or upload a waste image — EcoSort AI instantly classifies it
        and gives eco-friendly recycling tips.
    </p>
    <br>
</div>
""", unsafe_allow_html=True)

# --- BUTTON THAT OPENS CLASSIFIER PAGE ---
clicked = st.button("Try the Classifier 🚀")

if clicked:
    st.switch_page("pages/3_Classifier.py")

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#c8e6c9; font-size:15px;">
Developed by <b>Kavibharathi S</b><br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
