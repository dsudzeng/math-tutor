import streamlit as st
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import os
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title='🦜🔗 GenAI Math Tutor')
st.header('ARTIFICIAL INTELLIGENCE IN ORGANIZATIONS (BS)', divider='rainbow')
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;">The future of business</p>'
st.markdown(new_title, unsafe_allow_html=True)


st.write('**Students will learn to understand what artificial intelligence is, and what AI means for businesses and organizations and develop skills for applying artificial intelligence tools and methods in a variety of industries. With these skills, they will be prepared to help make data-driven decisions in their companies, optimize business processes and workflows, minimize costs, and maximize revenues by utilizing AI tools and applications. They will also be able to successfully navigate AI-related issues, challenges, and ethics in workplaces and be AI-aware in society.**')

#st.title('🦜🔗 Paradigm Futures Image Generator')
st.title('🦜🔗 GenAI Math Tutor')
txt_input = st.text_area('Enter your question', '', height=200)


interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant",
    instructions='''You are a personal math tutor. Write and run code to answer math questions. 
    // response rules
Writing math formulas:
You have a MathJax render environment.
- Any LaTeX text between single dollar sign ($) will be rendered as a TeX formula;
- Use $(tex_formula)$ in-line delimiters to display equations instead of backslash;
- The render environment only uses $ (single dollarsign) as a container delimiter, never output $$.
Example: $x^2 + 3x$ is output for "x² + 3x" to appear as TeX.`''',
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
input_dict = {}
input_dict ["content"] = txt_input
output = interpreter_assistant.invoke(input_dict)

i = 0
while i < len(output):
  st.info(output[i].content[0].text.value)
  i = i + 1

