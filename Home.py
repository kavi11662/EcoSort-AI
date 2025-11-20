import streamlit as st
from utils import *

st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="centered")

# CSS + Navbar
from utils import navbar
navbar()

st.markdown('<h1 class="title">♻ EcoSort AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart Waste Classification for a Cleaner Planet 🌿</p>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-top:50px;">
    <h2 style="color:#76ff03;">AI-powered Waste Segregation</h2>
    <p style="font-size:18px; color:#e8f5e9;">
    Upload an image or take a live picture — EcoSort AI will instantly classify the waste
    and suggest eco-friendly disposal tips.
    </p>
    <br>
    <a href="/Classifier" target="_self">
        <button style="padding:15px 30px; font-size:20px; background:#76ff03; 
                       border-radius:10px; border:none; cursor:pointer;">
            Try EcoSort AI 🚀
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
