import streamlit as st

# --- GLOBAL UI CSS ---
def global_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .navbar {
        display: flex;
        justify-content: center;
        gap: 40px;
        background: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        backdrop-filter: blur(4px);
    }
    .nav-item {
        color: #76ff03;
        font-size: 20px;
        font-weight: 600;
        text-decoration: none;
    }
    .nav-item:hover {
        color: #00e676;
    }
    .title {
        text-align:center; font-size:52px; font-weight:900;
        color:#76ff03;
        text-shadow:0 0 25px #76ff03, 0 0 40px #00e676;
    }
    .subtitle {
        text-align:center; font-size:18px; font-style:italic;
        color:#b9f6ca;
    }
    .result-card {
        background: rgba(255,255,255,0.08);
        padding: 30px;
        border-radius: 20px;
        margin-top: 25px;
        text-align: center;
    }
    .predicted { font-size:30px; color:#76ff03; font-weight:bold; }
    .confidence { font-size:20px; color:#b2ff59; }
    .tip { font-size:18px; color:#e8f5e9; margin-top:10px; }
    </style>
    """, unsafe_allow_html=True)


# --- NAVBAR FUNCTION ---
def navbar():
    st.markdown("""
    <div class="navbar">
        <a class="nav-item" href="/Home" target="_self">Home</a>
        <a class="nav-item" href="/About" target="_self">About</a>
        <a class="nav-item" href="/Features" target="_self">Features</a>
        <a class="nav-item" href="/Classifier" target="_self">EcoSort AI</a>
        <a class="nav-item" href="/Contact" target="_self">Contact</a>
    </div>
    """, unsafe_allow_html=True)
