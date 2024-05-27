import streamlit as st
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import os
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title='🦜🔗 GenAI Math Tutor')
st.title('🦜🔗 GenAI Math Tutor')
txt_input = st.text_area('Enter your question', '', height=200)


interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
input_dict = {}
input_dict ["content"] = txt_input
output = interpreter_assistant.invoke(input_dict)

i = 0
while i < len(output):
  st.markdown(output[i].content[0].text.value)
  i = i + 1
