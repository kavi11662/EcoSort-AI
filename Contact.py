import streamlit as st
from utils import navbar
from utils import global_css




st.set_page_config(page_title="Contact", page_icon="♻")
global_css()
navbar()

st.markdown('<h1 class="title">Contact</h1>', unsafe_allow_html=True)

st.write("""
### Developer  
**Kavibharathi S**

### Internship  
AICTE–Shell–Edunet Green Skills Internship 🌍

### Project  
EcoSort AI — Smart Waste Classification System
""")
