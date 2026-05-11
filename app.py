import streamlit as streamlit.components.v1 as components

with open("rehan.html", 'r', encoding='utf-8') as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
