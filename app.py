import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers # to call saved llama model

# Functions to get response from my Llama 2 model

def get_llama_response(input_text, np_words, blog_style):
    
    # LLama2 model
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",
                     model_type = 'llama',
                     config ={"temperature": 0.01, "max_new_tokens": 256})
    
    # Prompt Template
    prompt = PromptTemplate(
        input_variables=["input_text", "np_words", "blog_style"],
        template=f"""
        You are a Blog writer
        You have been given a task to write a blog on {input_text}.
        You have to write {np_words} words.
        The blog should be written in {blog_style} style.
        Write the blog.
        """,
    )

    # Generate the response from model

    response = llm(prompt.format(style = blog_style, text = input_text, n_words = np_words))
    print(response)
    return response

# Streamlit Framework

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🧑‍💻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generate the Blogs 🧑‍💻")

input_text = st.text_input("Enter the Blog topic to generate")

## Lets create some additional columns

col1, col2 = st.columns([5,5])

with col1:
    np_words = st.text_input("No of words")

with col2:
    blog_style = st.selectbox("Writing the blog for",('Data scientist', 'Researchers', 'Common people'), index=0)

submit = st.button("Generate Blog")

if submit:
    with st.spinner('Processing...'):
        # Your code for generating the blog goes here
        st.write(get_llama_response(input_text, np_words, blog_style))

