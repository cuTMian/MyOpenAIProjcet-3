import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

from langchain.memory import ConversationBufferMemory

def clone_chat_robot(prompt, memory, openai_api_key, openai_base_url=""):
    if openai_base_url:
        model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key, openai_api_base=openai_base_url)
    else:
        model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

def utils_test():
    api_key = os.getenv("OPENAI_API_KEY")
    memory = ConversationBufferMemory(return_messages=True)
    while True:
        text = input("输入：")
        if text.lower() in ['e','q','exit','quit']:
            break
        r = clone_chat_robot(text, memory, api_key)
        print(r)

if __name__ == '__main__':
    utils_test()
