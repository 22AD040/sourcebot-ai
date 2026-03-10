import streamlit as st
import streamlit.components.v1 as components

from chatbot.chat_manager import chat_with_bot
from database.db import SessionLocal
from database.models import Chat


def chat_page():

    st.title("SOURCEBOT AI")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.session_state.get("load_chat"):

        db = SessionLocal()

        chats = db.query(Chat).filter(
            Chat.conversation_id == st.session_state.conversation_id
        ).order_by(Chat.created_at).all()

        st.session_state.chat_history = []

        for c in chats:

            st.session_state.chat_history.append({
                "role": c.role,
                "content": c.message
            })

        st.session_state.load_chat = False

    for msg in st.session_state.chat_history:

        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])

        else:
            with st.chat_message("assistant"):
                st.write(msg["content"])

    user_input = st.chat_input("Ask anything...")

    if user_input:

        reply, history = chat_with_bot(
            st.session_state.chat_history,
            user_input,
            st.session_state.user.id
        )

        st.session_state.chat_history = history

        st.rerun()


    components.html(
        """
        <script>
        function scrollToBottom() {
            const chatContainer = parent.document.querySelector('.main');
            chatContainer.scrollTo({
                top: chatContainer.scrollHeight,
                behavior: 'smooth'
            });
        }
        </script>

        <button onclick="scrollToBottom()" 
        style="
        position: fixed;
        bottom: 40px;
        right: 40px;
        font-size: 22px;
        padding: 10px 14px;
        border-radius: 50%;
        background-color: #333;
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        ">
        ↓
        </button>
        """,
        height=0
    )