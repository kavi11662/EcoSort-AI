import streamlit as st
from utils import global_css

st.set_page_config(page_title="About", page_icon="ℹ️")

global_css()

# ----------- CUSTOM BACKGROUND IMAGE CSS -----------
st.markdown("""
<style>
.about-bg {
    background-image: url("background.jpg");
    background-size: cover;
    background-position: center;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 0 30px rgba(0,0,0,0.4);
}
.about-content {
    background: rgba(0, 0, 0, 0.55);
    padding: 25px;
    border-radius: 15px;
    color: #e8f5e9;
    font-size: 18px;
    line-height: 1.7;
}
.section-title {
    font-size: 32px;
    color: #76ff03;
    font-weight: 800;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ----------- TITLE -----------
st.markdown('<h1 class="title">About EcoSort AI</h1>', unsafe_allow_html=True)

# ----------- BACKGROUND BOX -----------
st.markdown('<div class="about-bg">', unsafe_allow_html=True)

st.markdown('<div class="about-content">', unsafe_allow_html=True)

st.write("""
EcoSort AI is a next-generation smart waste-classification system designed to bring automation,
accuracy, and sustainability into everyday waste management. Powered by advanced deep learning models,
EcoSort AI identifies **10 different types of waste materials in real time**, enabling faster and more reliable segregation.

By reducing human mistakes in waste sorting, the system prevents recyclable materials from ending up in landfills,
supports cleaner waste streams, and encourages responsible disposal practices.

Whether used in homes, institutions, public spaces, or businesses, EcoSort AI provides **instant eco-friendly guidance** to help users make informed decisions.
""")

st.markdown('<p class="section-title">Our Mission</p>', unsafe_allow_html=True)
st.write("""
To make sustainable living effortless by integrating AI into waste management and guiding communities
toward a cleaner, greener, and more circular future.
""")

st.markdown('<p class="section-title">Why It Matters</p>', unsafe_allow_html=True)
st.write("""
Improper waste segregation leads to:

- Increased landfill overflow  
- Higher pollution levels  
- Loss of recyclable resources  
- Greater strain on municipal systems  

EcoSort AI addresses these challenges with simple interactions, real-time predictions,
and eco-conscious recommendations — helping build a **smarter and more sustainable world**.
""")

st.markdown('</div>', unsafe_allow_html=True)  # close about content
st.markdown('</div>', unsafe_allow_html=True)  # close bg box
