import streamlit as st
from agent import agent

st.set_page_config(page_title="AI Math Tutor", page_icon="")

st.title("Math First-Principles Tutor")
st.markdown("I help you solve math problems and verify your logic using symbolic algebra.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask a math question (e.g., 'Is (x+1)^2 the same as x^2 + 2x + 1?')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # The agent runs and uses the MathVerificationTool if needed
            response = agent.run(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})