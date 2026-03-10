import streamlit as st

from ui.login_ui import login_page
from ui.sidebar import sidebar
from ui.chat_ui import chat_page


from database.db import engine
from database.models import Base

Base.metadata.create_all(bind=engine)


st.set_page_config(
    page_title="SOURCEBOT AI",
    page_icon="🤖",
    layout="wide"
)

if "user" not in st.session_state:
    st.session_state.user = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.session_state.user is None:

   
    login_page()

else:

   
    sidebar()

    chat_page()