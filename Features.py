import streamlit as st
from utils import navbar
from utils import global_css




st.set_page_config(page_title="Features", page_icon="♻")
global_css()
navbar()

st.markdown('<h1 class="title">Features</h1>', unsafe_allow_html=True)

st.write("""
### ✅ 10-Class Waste Detection  
### ✅ Upload Image or Live Camera Capture  
### ✅ Eco-friendly Disposal Tips  
### ✅ Neon Dark Professional UI  
### ✅ HuggingFace-powered Deep Learning Model  
""")
