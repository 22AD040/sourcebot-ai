def update_memory(history, user_msg, bot_msg):

    history.append({
        "role": "user",
        "content": user_msg
    })

    history.append({
        "role": "assistant",
        "content": bot_msg
    })

    return history