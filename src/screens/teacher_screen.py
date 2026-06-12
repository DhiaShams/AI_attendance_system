import streamlit as st

from src.ui.base_layout import style_bg_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.database.db import check_teacher_exist,create_teacher,teacher_login

def register_teacher(tr_username,tr_name,tr_pwd,tr_confirm_pwd):
    if not tr_username or not tr_name or not tr_pwd:
        return False,"All fields are required!"
    if check_teacher_exist(tr_username):
        return False,"Username already taken!"
    if tr_pwd!=tr_confirm_pwd:
        return False,"Passwords doesn't match!"
    
    try:
        create_teacher(tr_username,tr_pwd,tr_name)
        return True,"Successfully Created User! Login Now"
    except Exception as e:
        return False,"Unexpected error!"

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

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data

    st.header(
        f"""
            Welcome,{teacher_data['name']}
    """)

def login_tr(tr_username,tr_pwd):
    if not tr_username or not tr_pwd:
        return False
    
    teacher=teacher_login(tr_username,tr_pwd)

    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True

def teacher_screen_login():
    
    st.header('Login using password',text_alignment='center')
    
    st.space()
    st.space()

    tr_username=st.text_input("Enter username",placeholder="xyz123")
    tr_pwd=st.text_input("Enter password",type="password",placeholder="Enter password")

    st.divider()

    btn1,btn2=st.columns(2)

    with btn1:
        if st.button('Login Now',icon=':material/passkey:',shortcut='control+enter',width='stretch'):
            if login_tr(tr_username,tr_pwd):
                st.toast("Welcome back!",icon="👋")
                import time
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid credentials")

    with btn2:
        if st.button('Register Instead',icon=':material/passkey:',width='stretch',type='primary'):
            st.session_state.teacher_login_type="register"

def teacher_screen_register():
    
    st.header('Register your teacher profile',text_alignment='center')
    
    st.space()
    st.space()

    tr_username=st.text_input("Enter username",placeholder="@aneeta")
    tr_name=st.text_input("Enter name",placeholder="Aneeta Rose")
    tr_pwd=st.text_input("Enter password",type="password",placeholder="Enter password")
    tr_confirm_pwd=st.text_input("Confirm password",type="password",placeholder="Confirm your password")

    st.divider()

    btn1,btn2=st.columns(2)

    
    with btn1:
        if st.button('Register Now',icon=':material/passkey:',width='stretch',type='primary',shortcut='control+enter'):
            success,msg=register_teacher(tr_username,tr_name,tr_pwd,tr_confirm_pwd)
            if success:
                st.success(msg)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(msg)

    with btn2:
        if st.button('Login Instead',icon=':material/passkey:',width='stretch'):
            st.session_state.teacher_login_type="login"

