import streamlit as st
from utils import navbar

st.set_page_config(page_title="About EcoSort", page_icon="♻")

navbar()

st.markdown('<h1 class="title">About EcoSort AI</h1>', unsafe_allow_html=True)

st.write("""
EcoSort AI is designed to solve the growing challenge of improper waste segregation.
With increasing landfill pressure and pollution, it is essential to support people with
a simple, instant waste identification tool.

EcoSort AI uses deep learning to classify **10 types of waste** and offers **disposal tips**
for better environmental practices.
""")
