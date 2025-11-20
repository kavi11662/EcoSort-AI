import streamlit as st
from utils import global_css

st.set_page_config(page_title="About", page_icon="ℹ️")
global_css()

st.markdown('<h1 class="title">About EcoSort AI</h1>', unsafe_allow_html=True)

st.write("""
EcoSort AI solves the real problem of improper waste segregation by using deep learning  
to classify **10 types of waste** and provide correct disposal guidance.

Its mission is to reduce pollution, support recycling, and promote clean surroundings.
""")
