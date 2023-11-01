import streamlit as st

import requests


# Function for generating response from LLMSetve
def generate_response(prompt_input):
    inputs = {"input": {"question": prompt_input}}
    response = requests.post("https://c007-91-174-165-234.ngrok-free.app/invoke", json=inputs)

    return response.json()["output"]["answer"]

# App title
st.set_page_config(page_title="A LangChain Chatbot")


# Store utterances
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is from user
if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Consulting oracles..."):
            response = generate_response(prompt)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
