class MessageUtil:
    def __init__(self):
        self.messages = [{"role": "ai", "msg": "开始对话吧"}]

    def write(self, role, msg, st):
        message = {"role": role, "msg": msg}
        self.messages.append(message)
        st.chat_message(role).write(msg)

    def get(self):
        return self.messages

    def reset(self):
        self.messages = [{"role": "ai", "msg": "开始对话吧"}]

message_util = MessageUtil()
