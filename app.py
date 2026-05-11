import streamlit as st
import streamlit.components.v1 as components

# HTML file ko read karna
try:
    with open("rehan.html", 'r', encoding='utf-8') as f:
        html_code = f.read()
    
    # HTML ko Streamlit app mein dikhana
    components.html(html_code, height=1000, scrolling=True)
except FileNotFoundError:
    st.error("rehan.html file nahi mili. Check karein ke file GitHub par uploaded hai.")
