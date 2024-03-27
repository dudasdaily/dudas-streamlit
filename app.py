import streamlit as st

x = st.slider("select a value")
st.write(x, ' is square', x*x)