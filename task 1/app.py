import streamlit as st # For the app UI
from langchain_groq import ChatGroq # For the llm model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage # For storing the messages
from dotenv import load_dotenv # For the API keys
import os # Again, for the api keys
import re # To remove the think block

# Loading the  API keys
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Function to remove the think block for my respone:
def clean_response(response):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

# Persona prompts
PERSONAS = {
    "Default": "You are a helpful assistant. Please respond to the user queries in a formal way.",
    "RoastBot": "You are RoastBot. Always respond with witty, sarcastic roasts no matter what the user says.",
    "ShakespeareBot": "You are ShakespeareBot. Respond to all queries in Shakespeare-style old English prose.",
    "Emoji Translator": "You are EmojiBot. Translate everything into emoji-speak.",
    "Creative": "You are a highly creative assistant who replies in imaginative, playful ways using metaphors."
}

# Function to generate context-aware responses
def generate_response(question, llm_name, chat_history, persona_prompt):
    model = ChatGroq(model=llm_name)

    # Creating list to store a single system message which is the persona instruction
    messages = [
        SystemMessage(content=persona_prompt)
    ]

    # Adding chat history. Storing the user input in HumanMessage and bot response in AIMessage
    for role, msg in chat_history:
        if role == "user":
            messages.append(HumanMessage(content=msg))
        elif role == "bot":
            messages.append(AIMessage(content=msg))

    # Creating space for the new user input
    messages.append(HumanMessage(content=question))

    # Invoking the chosen model
    response = model.invoke(messages)
    return response.content

# App UI
st.set_page_config(page_title="Persona AI Chatbot", layout="wide", initial_sidebar_state="expanded")
st.title("🤖 SRIKA-Your AI friend")

# Selector for choosing the llm model
llm_model = st.sidebar.selectbox("Choose a model", [
    "deepseek-r1-distill-llama-70b",
    "moonshotai/kimi-k2-instruct",
    "meta-llama/llama-4-scout-17b-16e-instruct"
])
# Selector for choosing the persona of the bot
persona_choice = st.sidebar.selectbox("Choose a persona", list(PERSONAS.keys()))

# Initialising chat history in this session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Store user input as user (HumanMessage)
    st.session_state.chat_history.append(("user", user_input))

    # Getting persona- specific response
    bot_response = generate_response(
        user_input,
        llm_model,
        st.session_state.chat_history,
        PERSONAS[persona_choice]
    )
    bot_response = clean_response(bot_response)

    # Store bot response in AIMessage
    st.session_state.chat_history.append(("bot", bot_response))

# Printing the message
for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

