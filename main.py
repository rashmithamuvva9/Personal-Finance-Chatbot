import streamlit as st
from chatbot_logic import ChatbotLogic

# Initialize chatbot
chatbot = ChatbotLogic()

st.set_page_config(page_title="Personal Finance Chatbot", layout="wide")

st.title("Your Personal Finance AI Assistant")

# Sidebar for user profile input
with st.sidebar:
    st.header("Your Profile")
    user_name = st.text_input("Name", "John Doe")
    user_age = st.number_input("Age", 18, 100, 30)
    user_occupation = st.selectbox("Occupation", ["Student", "Professional", "Retired", "Other"])
    # ... more profile inputs

    if st.button("Update Profile"):
        chatbot.user_profile.update_profile(name=user_name, age=user_age, occupation=user_occupation)
        st.success("Profile updated!")

# Main chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me about savings, taxes, or investments..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = chatbot.get_response(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})