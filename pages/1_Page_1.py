import streamlit as st
from utils_module.utils import myfunc

st.write("You can change me, but those changes WILL NOT be detected.")

if st.button('Press me'):
    message = myfunc()
    st.write(message)
