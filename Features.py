import streamlit as st
from utils import navbar, global_css

st.set_page_config(page_title="Features", page_icon="♻")

global_css()
navbar()

st.markdown('<h1 class="title">Features</h1>', unsafe_allow_html=True)

st.write("""
### ✅ 10-Class Waste Detection  
### ✅ Upload Image or Live Camera  
### ✅ Instant Eco-Friendly Tips  
### ✅ HuggingFace Model Integration  
### ✅ Neon Dark Professional UI  
### ✅ Multi-Page Website Navigation  
""")
