import streamlit as st
from utils import global_css

st.set_page_config(page_title="About", page_icon="ℹ️")
global_css()

st.markdown('<h1 class="title">About EcoSort AI</h1>', unsafe_allow_html=True)

st.write("""
EcoSort AI is a next-generation smart waste-classification system designed to bring 
automation, accuracy, and sustainability into everyday waste management. Powered by 
advanced deep learning models, EcoSort AI identifies **10 different types of waste 
materials** in real time, enabling faster and more reliable segregation.

By reducing human error in waste sorting, the system helps prevent recyclable materials 
from ending up in landfills, supports cleaner waste streams, and encourages responsible 
disposal practices. Whether used in homes, institutions, public spaces, or businesses, 
EcoSort AI provides instant eco-friendly guidance to help users make informed decisions.

### **Our Mission**
To make sustainable living effortless by integrating AI into waste management and 
driving communities toward a cleaner, greener, and more circular future.

### **Why It Matters**
Improper waste segregation leads to:
- Increased landfill overflow  
- Higher pollution levels  
- Loss of recyclable resources  
- Greater strain on municipal systems  

EcoSort AI addresses these challenges with simple interactions, real-time predictions, 
and environmentally conscious recommendations — helping build a smarter and more 
sustainable world.
""")
