import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

def clone_chat_robot(text, memory, openai_api_key, openai_base_url=""):
    if openai_base_url:
        model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key, openai_api_base=openai_base_url)
    else:
        model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位脾气暴躁的助手，喜欢冷嘲热讽和用阴阳怪气的语气回答问题。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = ConversationChain(llm=model, memory=memory, prompt=prompt)

    response = chain.invoke({"input": text})
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
