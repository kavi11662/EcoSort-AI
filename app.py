import streamlit as st
from utils import global_css

# --- PAGE SETTINGS ---
st.set_page_config(page_title="EcoSort AI", page_icon="♻", layout="wide")

# --- APPLY GLOBAL STYLING ---
global_css()

# --- HOME HERO SECTION ---
st.markdown(f"""
<style>
/* Full-screen background */
[data-testid="stAppViewContainer"] {{
    background: url("https://image.shutterstock.com/image-photo/waste-management-background-260nw-xxxxxx.jpg") no-repeat center center fixed;
    background-size: cover;
}}

/* Hero content container */
.hero {{
    background: rgba(0, 0, 0, 0.5);  /* Semi-transparent overlay */
    padding: 80px 40px;
    border-radius: 20px;
    max-width: 800px;
    margin: 50px auto;
    text-align: center;
}}

/* Title and subtitle styling */
.hero h1 {{
    font-size: 64px;
    color: #76ff03;
    font-weight: 900;
    text-shadow: 0 0 25px #76ff03, 0 0 40px #00e676;
    margin-bottom: 20px;
}}
.hero p {{
    font-size: 20px;
    color: #e8f5e9;
    line-height: 1.6;
    margin-bottom: 30px;
}}

/* Button styling */
.hero button {{
    padding: 15px 40px;
    font-size: 22px;
    background: #76ff03;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    transition: transform 0.2s;
}}
.hero button:hover {{
    transform: scale(1.05);
}}
</style>

<div class="hero">
    <h1>♻ EcoSort AI</h1>
    <p>Smart Waste Classification for a Cleaner Planet 🌿<br>
    Capture or upload a waste image — EcoSort AI instantly identifies the waste type
    and provides eco-friendly recycling and disposal tips.</p>
    <button onclick="window.location.href='/3_Classifier'">Try the Classifier 🚀</button>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; margin-top:50px; color:#c8e6c9; font-size:15px;">
Developed by <b>Kavibharathi S</b><br>
"Clean surroundings, clear mind — Let’s build a greener tomorrow 🌱"
</div>
""", unsafe_allow_html=True)
