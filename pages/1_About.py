import streamlit as st
from utils import global_css
import base64

st.set_page_config(page_title="About EcoSort AI", page_icon="ℹ️", layout="wide")
global_css()

# ===== BACKGROUND IMAGE =====
bg_image_path = "assets/about_bg.jpg"

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_bg = get_base64_image(bg_image_path)

# ===== FULL PAGE BACKGROUND + CONTENT STYLING =====
st.markdown(
    f"""
    <style>

    /* FULL PAGE BACKGROUND */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(rgba(0,0,0,0.40), rgba(0,0,0,0.50)),
        url("data:image/png;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* HERO SECTION */
    .about-hero {{
        padding: 180px 20px;
        text-align: center;
        color: white;
    }}

    .about-title {{
        font-size: 58px;
        font-weight: 900;
        text-shadow: 0 0 25px black;
        margin-bottom: 25px;
    }}

    .about-desc {{
        max-width: 950px;
        margin: auto;
        font-size: 22px;
        line-height: 1.8;
        color: #e8f5e9;
        text-shadow: 0 0 12px black;
    }}

    /* SECTION HEADINGS */
    .section-title {{
        font-size: 38px;
        font-weight: 800;
        margin-top: 60px;
        text-align: center;
        color: #76ff03;
    }}

    /* PARAGRAPH TEXT */
    .section-text {{
        max-width: 900px;
        margin: auto;
        font-size: 20px;
        color: #e8f5e9;
        line-height: 1.8;
        text-align: center;
        padding: 10px 20px;
    }}

    /* DIVIDER */
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

# =================== HERO SECTION ===================
st.markdown(
    """
    <div class="about-hero">
        <h1 class="about-title">About EcoSort AI</h1>

        <p class="about-desc">
            EcoSort AI is a next-generation smart waste classification system designed to bring 
            automation, accuracy, and sustainability into everyday waste management.
            Powered by advanced deep learning models, EcoSort AI identifies 
            <b>10 different types of waste in real time</b>, enabling faster and more reliable segregation.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =================== BODY CONTENT ===================
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Our Mission</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class="section-text">
        To make sustainable living effortless by integrating AI into waste management 
        and guiding communities toward a cleaner, greener, and more circular future.
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
        • Increased landfill overflow <br>
        • Higher pollution levels <br>
        • Loss of recyclable resources <br>
        • Strain on municipal systems <br><br>

        EcoSort AI solves these problems with <b>real-time predictions</b> and 
        <b>eco-friendly recommendations</b> — helping build a smarter and more sustainable world.
    </p>
    """,
    unsafe_allow_html=True
)
