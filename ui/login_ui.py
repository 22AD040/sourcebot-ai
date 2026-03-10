import streamlit as st
from auth.login import login_user
from auth.signup import create_user

def login_page():

  
    left, center, right = st.columns([3,1,3])
    with center:
        st.image("static/logo.png", width=800)

   
    st.markdown(
        "<h1 style='text-align:center;font-size:60px; margin-top:-10px; margin-bottom:0;'>SOURCEBOT AI</h1>",
        unsafe_allow_html=True
    )

    
    st.markdown(
        "<p style='text-align:center; font-size:30px; color:gray; margin-top:0;'>Source for All Solutions,The Only Bot SOURCEBOT </p>",
        unsafe_allow_html=True
    )
    tab1, tab2 = st.tabs(["Login", "Signup"])

  
    with tab1:

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):

            user = login_user(email, password)

            if user:
                st.session_state.user = user
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid email or password")

    
    with tab2:

        name = st.text_input("Name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")

        if st.button("Create Account"):

            success = create_user(name, email, password)

            if success:
                st.success("Account created! Please login.")
            else:
                st.error("User already exists")