

import streamlit as st
from models import GPT3, DALLE2, Codex, ChatGPT
from utils import preprocess, get_context, decode_response


def main():
    st.set_page_config(page_title="Mental Health Chatbot")
    st.title("Mental Health Chatbot")

    # Initialize models
    gpt3 = GPT3()
    dalle2 = DALLE2()
    codex = Codex()
    chatgpt = ChatGPT()

    # Get user input
    input_text = st.text_input("You:", key="input_text")

    if input_text:
        # Preprocess user input
        input_text = preprocess(input_text)

        # Select context based on user input
        context = get_context(input_text)

        # Generate response based on selected context
        
        if context == "GPT-3":
            response = gpt3.generate_response(input_text)
        elif context == "DALL-E 2":
            response = dalle2.generate_response(input_text)
        elif context == "Codex":
            response = codex.generate_response(input_text)
        elif context == "ChatGPT":
            response = chatgpt.generate_response(input_text)

        # Decode response and display to user
        decoded_response = decode_response(response)
        st.text_area("Bot:", value=decoded_response, height=150, key="bot_response")


if __name__ == "__main__":
    main()
