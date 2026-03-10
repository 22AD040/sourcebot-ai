import streamlit as st
from database.db import SessionLocal
from database.models import Chat


def sidebar():

    with st.sidebar:

        st.title("SOURCEBOT AI")

       
        if st.button("➕ New Chat"):
            st.session_state.chat_history = []
            st.session_state.conversation_id = None
            st.rerun()

        st.divider()
        st.subheader("Previous Chats")

        db = SessionLocal()
        user_id = st.session_state.user.id

        conversations = db.query(Chat).filter(
            Chat.user_id == user_id,
            Chat.role == "user"
        ).order_by(Chat.created_at.desc()).all()

        seen = set()

        for chat in conversations:

            if chat.conversation_id in seen:
                continue

            seen.add(chat.conversation_id)

            title = chat.message[:40]

            if st.button(title, key=chat.conversation_id):

                st.session_state.conversation_id = chat.conversation_id
                st.session_state.load_chat = True

                st.rerun()

        st.divider()

        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()