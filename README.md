# ACM-GEN-AI-INDUCTION-2024A2PS1190H
# Task 1:
# I used 3 groq models (deepseek, llama, moonshot) which is the user's choice.
# I loaded the API keys of langchain and groq into the .env files.
# I added the persona prompts as key:value pairs and sent the keys for user input
# I made an additional function to remove the think block of the model during response.
# I am holding context across messages by storing the inputs and responses using HumanMessage and AIMessage.
# I am initialising the conversation using SystemMessage
# I am storing the above operation as a function because it makes it easy for me to call this function when I am building my streamlit app.
# In the app, I am making a session history list and storing the respective user input and bot response.
# Hope you like it :-)
