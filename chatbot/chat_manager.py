from chatbot.groq_client import ask_groq
from database.db import SessionLocal
from database.models import Chat
import uuid
import datetime
import streamlit as st


def save_message(user_id, conversation_id, role, message):

    db = SessionLocal()

    chat = Chat(
        user_id=user_id,
        conversation_id=conversation_id,
        role=role,
        message=message,
        created_at=datetime.datetime.utcnow()
    )

    db.add(chat)
    db.commit()


def chat_with_bot(history, message, user_id):

    if "conversation_id" not in st.session_state or st.session_state.conversation_id is None:
        st.session_state.conversation_id = str(uuid.uuid4())

    conversation_id = st.session_state.conversation_id

  
    history.append({
        "role": "user",
        "content": message
    })

    save_message(user_id, conversation_id, "user", message)

    reply = ask_groq(history)

    history.append({
        "role": "assistant",
        "content": reply
    })

    save_message(user_id, conversation_id, "assistant", reply)

    return reply, history