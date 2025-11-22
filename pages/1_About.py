import streamlit as st
from utils import global_css
import base64

st.set_page_config(page_title="About EcoSort AI", page_icon="ℹ️", layout="wide")
global_css()

# ====== LOAD BACKGROUND IMAGE ======
bg_image_path = "assets/about_bg.jpg"

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

encoded_bg = get_base64(bg_image_path)

# ====== PROFESSIONAL UI CSS ======
st.markdown(
    f"""
<style>

[data-testid="stAppViewContainer"] {{
    background: linear-gradient(to bottom, #072026, #0f2f39);
}}

.hero-section {{
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.55), 
        rgba(0, 0, 0, 0.55)
    ),
    url("data:image/png;base64,{encoded_bg}");
    background-size: cover;
    background-position: center;
    padding: 170px 20px;
    text-align: center;
    color: white;
}}

.hero-title {{
    font-size: 60px;
    font-weight: 900;
    margin-bottom: 20px;
    text-shadow: 0 0 25px black;
}}

.hero-desc {{
    max-width: 950px;
    margin: auto;
    font-size: 22px;
    line-height: 1.8;
    color: #e8f5e9;
    text-shadow: 0 0 10px rgba(0,0,0,0.8);
}}

.hero-btn {{
    background-color: #76ff03;
    padding: 14px 35px;
    font-size: 20px;
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    cursor: pointer;
    margin-top: 25px;
    transition: 0.3s;
}}

.hero-btn:hover {{
    background-color: #00e676;
    transform: scale(1.05);
    box-shadow: 0 0 18px #76ff03;
}}

.section-title {{
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    margin-top: 70px;
    margin-bottom: 10px;
    color: #76ff03;
}}

.section-text {{
    max-width: 900px;
    margin: auto;
    text-align: center;
    line-height: 1.8;
    font-size: 20px;
    color: #e8f5e9;
    padding: 10px 20px;
}}

.divider {{
    width: 70%;
    height: 2px;
    margin: 45px auto;
    background: linear-gradient(to right, transparent, #76ff03, transparent);
}}

</style>
""",
    unsafe_allow_html=True
)

# ===== HERO SECTION ======
st.markdown(
    """
<div class="hero-section">
    <h1 class="hero-title">About EcoSort AI</h1>

    <p class="hero-desc">
        EcoSort AI is a next-generation smart waste classification system designed to bring 
        automation, accuracy, and sustainability into everyday waste management. Powered by 
        advanced deep learning models, it identifies <b>10 types of waste in real time</b>, ensuring 
        fast and reliable segregation for homes, institutions, public spaces, and businesses.
    </p>

    <a href="/3_Classifier" target="_self">
        <button class="hero-btn">Try the Classifier 🚀</button>
    </a>
</div>
""",
    unsafe_allow_html=True
)

# ===== BODY CONTENT ======
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Our Mission</h2>", unsafe_allow_html=True)
st.markdown(
    """
<p class="section-text">
    To make sustainable living effortless by integrating AI into waste management and guiding 
    communities toward a cleaner, greener, and more circular future.
</p>
""",
    unsafe_allow_html=True
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Why It Matters</h2>", unsafe_allow_html=True)
st.markdown(
    """
<p class="section-text">
    Improper waste segregation leads to:<br><br>
    • Increased landfill overflow<br>
    • Higher pollution levels<br>
    • Loss of recyclable resources<br>
    • Heavy strain on municipal systems<br><br>

    EcoSort AI solves these challenges with <b>real-time waste classification</b> and 
    <b>eco-friendly disposal recommendations</b> — helping build a smarter and more sustainable world.
</p>
""",
    unsafe_allow_html=True
)


