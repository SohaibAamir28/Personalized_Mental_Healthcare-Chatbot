import streamlit as st
from chatbot import ChatBot

def main():
    st.set_page_config(page_title="Mental Healthcare Chatbot", page_icon=":brain:")
    st.title("Mental Healthcare Chatbot")
    chatbot = ChatBot()
    user_input = st.text_input("You: ")
    if user_input:
        bot_response = chatbot.generate_response(user_input)
        st.write("Bot: ", bot_response)

if __name__ == "__main__":
    main()
