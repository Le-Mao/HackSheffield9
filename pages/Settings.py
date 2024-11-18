import streamlit as st 
st.set_page_config(
    page_title="Settings",
    page_icon=":gear:",
    layout="wide",
)

st.title("Settings")

st.subheader("Customize Your App")
theme = st.selectbox("Choose Theme", ["Light", "Dark", "System Default"])
st.slider("Adjust brightness", min_value=0, max_value=100, value=50)

st.text("Additional settings can go here.")