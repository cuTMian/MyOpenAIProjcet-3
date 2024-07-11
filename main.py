import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import clone_chat_robot
from message_utils import message_util

st.title("聊天机器人")
with st.sidebar:
    openai_api_key = st.text_input('请输入您的OpenAI API密钥', type='password')
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/api-keys)")
    openai_base_url = st.text_input('如果需要，您可以输入您的api base url')
    clear = st.button("清空对话内容和记忆")

if "memory" not in st.session_state or clear:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    message_util.reset()

for message in message_util.get():
    st.chat_message(message["role"]).write(message["msg"])

msg = st.chat_input()
if msg:
    warning_msg = ""
    if not openai_api_key:
        warning_msg = "请输入您的OpenAI API密钥！"
    elif not msg:
        warning_msg = "您得说两句"

    if warning_msg:
        st.info(warning_msg)
        st.stop()
    else:
        message_util.write("human", msg, st)
        with st.spinner(("AI思考中，请稍等...")):
            response = clone_chat_robot(msg, st.session_state["memory"], openai_api_key, openai_base_url)
            message_util.write("ai", response, st)
