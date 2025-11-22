import streamlit as st
from utils import global_css
import base64

st.set_page_config(page_title="About EcoSort AI", page_icon="ℹ️")
global_css()

# Background image path
bg_image_path = "assets/about_bg.jpg"

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert image to base64
encoded_bg = get_base64_image(bg_image_path)

# Apply fullscreen background image
st.markdown(
    f"""
    <style>
    .about-hero {{
        background-image: url("data:image/jpg;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        padding: 180px 20px;
        border-radius: 0px;
        text-align: center;
        color: white;
    }}

    .about-title {{
        font-size: 50px;
        font-weight: 900;
        text-shadow: 0 0 15px black;
    }}

    .about-desc {{
        max-width: 850px;
        margin: auto;
        font-size: 20px;
        line-height: 1.7;
        text-shadow: 0 0 12px black;
    }}

    .section-title {{
        font-size: 35px;
        font-weight: 800;
        margin-top: 40px;
        color: #76ff03;
        text-align: center;
    }}

    .section-text {{
        max-width: 900px;
        margin: auto;
        font-size: 19px;
        line-height: 1.6;
        color: #e8f5e9;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    f"""
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

# Body Sections
st.markdown("<h2 class='section-title'>Our Mission</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='section-text'>"
    "To make sustainable living effortless by integrating AI into waste management "
    "and guiding communities toward a cleaner, greener, and more circular future."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<h2 class='section-title'>Why It Matters</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class='section-text'>
    Improper waste segregation leads to:
    <br><br>
    • Increased landfill overflow <br>
    • Higher pollution levels <br>
    • Loss of recyclable resources <br>
    • Strain on municipal systems <br><br>

    EcoSort AI solves these problems with real-time predictions and simple interactions—helping 
    build a smarter and more sustainable world.
    </p>
    """,
    unsafe_allow_html=True
)
