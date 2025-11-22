import streamlit as st
from utils import global_css
import base64

st.set_page_config(page_title="About EcoSort AI", page_icon="ℹ️")
global_css()

# Path to your uploaded background image
bg_image_path = "assets/about_bg.jpg"

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

encoded_bg = get_base64_image(bg_image_path)

# ---------- CUSTOM CSS -----------
st.markdown(
    f"""
    <style>
    .hero-section {{
        background-image: url("data:image/png;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 180px 30px;
        text-align: center;
        border-radius: 0px;
        box-shadow: inset 0 0 80px rgba(0,0,0,0.6);
    }}

    .hero-title {{
        font-size: 55px;
        font-weight: 900;
        color: white;
        text-shadow: 0 0 20px black;
    }}

    .hero-desc {{
        max-width: 900px;
        margin: auto;
        font-size: 22px;
        line-height: 1.7;
        color: #f1f8e9;
        text-shadow: 0 0 12px black;
    }}

    .hero-buttons button {{
        background-color: #76ff03;
        color: black;
        padding: 12px 30px;
        font-size: 20px;
        border-radius: 8px;
        border: none;
        margin-top: 20px;
        cursor: pointer;
        font-weight: bold;
    }}

    .section-title {{
        font-size: 36px;
        font-weight: 800;
        margin-top: 60px;
        text-align: center;
        color: #76ff03;
    }}

    .section-text {{
        max-width: 900px;
        margin: auto;
        font-size: 19px;
        color: #e8f5e9;
        text-align: center;
        line-height: 1.7;
        padding: 10px 20px;
    }}

    .divider {{
        width: 70%;
        height: 2px;
        margin: 40px auto;
        background: linear-gradient(to right, transparent, #76ff03, transparent);
    }}
    </style>
""",
    unsafe_allow_html=True
)

# ------------ HERO SECTION -----------
st.markdown(
    """
    <div class="hero-section">
        <h1 class="hero-title">About EcoSort AI</h1>
        <p class="hero-desc">
            EcoSort AI is a next-generation smart waste classification system designed to bring 
            automation, accuracy, and sustainability into everyday waste management.
            Powered by advanced deep learning models, it identifies 
            <b>10 different types of waste in real time</b>, ensuring faster and more reliable segregation.
        </p>

        <div class="hero-buttons">
            <a href="/3_Classifier" target="_self">
                <button>Try the Classifier 🚀</button>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------ BODY SECTION -----------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Our Mission</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class='section-text'>
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
    <p class='section-text'>
        Improper waste segregation leads to:<br><br>
        • Increased landfill overflow<br>
        • Higher pollution levels<br>
        • Loss of recyclable resources<br>
        • Heavy strain on municipal systems<br><br>

        EcoSort AI tackles these challenges with real-time waste classification and 
        eco-friendly recommendations — helping build a smarter and more sustainable world.
    </p>
    """,
    unsafe_allow_html=True
)
