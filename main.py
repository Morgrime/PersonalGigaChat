import streamlit as st 

from gigachatapi import get_access_token, send_prompt, sent_prompt_check

CLIENT_ID = st.secrets["CLIENT_ID"]
SECRET = st.secrets["SECRET"]

st.title("Not Chat-bot")

if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast("Токен получен")
    except Exception as e:
        st.toast(f"Токен не был получен: {e}")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "Чего надо?", "function_call": "auto"}]

# отправка сообщений
# TODO: добавить куда-то "function_call": "auto" для генерации картинок
for msg in st.session_state.messages:
    if msg.get("is_image"): # если был запрос на картинку
        st.chat_message(msg["role"]).image(msg["content"])
    else: # если на текст
        st.chat_message(msg["role"]).write(msg["content"])


if user_prompt := st.chat_input():
    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    with st.spinner("Происходит магия..."):
        response, is_image = sent_prompt_check(user_prompt, st.session_state.access_token)
        if is_image:
            st.chat_message("ai").image(response)
            st.session_state.messages.append({"role": "ai", "content": response, "is_image": True})
        else:
            st.chat_message("ai").write(response)
            st.session_state.messages.append({"role": "ai", "content": response})