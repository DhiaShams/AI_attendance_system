import streamlit as st

from src.ui.base_layout import style_bg_dashboard,style_base_layout
from src.components.header import header_dashboard

def teacher_screen():
    style_bg_dashboard()
    style_base_layout()

    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home" ,type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

def teacher_screen_login():
    
    st.header('Login using password')
    
    st.space()
    st.space()

    tr_username=st.text_input("Enter username",placeholder="xyz123")
    tr_pwd=st.text_input("Enter password",type="password",placeholder="Enter password")

    st.divider()

    btn1,btn2=st.columns(2)

    with btn1:
        st.button('Login Now',icon=':material/passkey:',shortcut='control+enter',width='stretch')

    with btn2:
        if st.button('Register Instead',icon=':material/passkey:',width='stretch',type='primary'):
            st.session_state.teacher_login_type="register"

def teacher_screen_register():
    
    st.header('Register your teacher profile')
    
    st.space()
    st.space()

    st_username=st.text_input("Enter username",placeholder="@aneeta")
    st_name=st.text_input("Enter name",placeholder="Aneeta Rose")
    st_pwd=st.text_input("Enter password",type="password",placeholder="Enter password")
    st_confirm_pwd=st.text_input("Confirm password",type="password",placeholder="Confirm your password")

    st.divider()

    btn1,btn2=st.columns(2)

    
    with btn1:
        st.button('Register Now',icon=':material/passkey:',width='stretch',type='primary',shortcut='control+enter')

    with btn2:
        if st.button('Login Instead',icon=':material/passkey:',width='stretch'):
            st.session_state.teacher_login_type="login"

