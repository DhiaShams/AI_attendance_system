import streamlit as st

from src.ui.base_layout import style_bg_dashboard,style_base_layout
from src.components.header import header_dashboard
from PIL import Image
import numpy as np

def student_screen():
    style_bg_dashboard()
    style_base_layout()

    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home" ,type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login with FaceID",text_alignment='center')
    st.space()
    st.space()

    photo_src=st.camera_input("Position your face in the center")
    if photo_src:
        np.array(Image.open())