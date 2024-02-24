import streamlit as st
from parser_google import selen_func



if st.button('Показать приветствие'):
    # Отображение приветственного сообщения
    st.write(selen_func())