import streamlit as st

x = st.slider("select a value")
st.write(x*x, ' is square of ', x)