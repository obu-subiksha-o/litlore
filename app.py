import streamlit as st
from ai_engine import analyze_text, what_if_generator

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("syles.css")

# Center logo + heading
st.markdown("<h1>📚 LitLore.AI</h1>", unsafe_allow_html=True)
st.markdown("<h2>Your candlelit companion into literary shadows</h2>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Input area
user_input = st.text_area("Paste a literary passage below:", height=250)

# Analyze Button
if st.button("Analyze Text"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = analyze_text(user_input)
            st.markdown("### Literary Analysis")
            st.write(result)
    else:
        st.warning("Paste something to analyze.")

# What If Button
if st.button("Generate 'What If' Scenario"):
    if user_input.strip():
        with st.spinner("Reimagining your passage..."):
            result = what_if_generator(user_input)
            st.markdown("### Alternate Scenario")
            st.write(result)
    else:
        st.warning("Paste something to twist.")
