import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Page configuration
st.set_page_config(
    page_title="AI Code Generator",
    layout="wide"
)

# Custom CSS for pro look
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stTextArea textarea {
            height: 150px !important;
        }
        .codebox {
            background-color: #f1f3f4;
            padding: 1.2rem;
            border-radius: 0.5rem;
        }
        .stButton button {
            background-color: #0072ff;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("##  AI-Powered Code & Test Generator")
st.write("Describe your coding task and let the AI generate both the implementation and the test cases.")

# Input Form
with st.form("code_form", clear_on_submit=False):
    col1, col2 = st.columns([1, 3])

    with col1:
        language = st.selectbox(
            " Choose a programming language",
            ["Python", "C++", "TypeScript", "C", "java", "Ruby", "Go", "Rust", "JavaScript","PHP", "Swift","Kotlin", "C#"]
        )
    with col2:
        task = st.text_area(
            " Describe the task",
            placeholder="E.g., Create a function that finds the median of a list of numbers"
        )

    submitted = st.form_submit_button(" Generate Code")

    if submitted:
        if not task.strip():
            st.error(" Please enter a task description.")
        else:
            # Prompt templates
            code_prompt = PromptTemplate(
                template="Write a {language} code that will perform the following task: {task} (return only the code, no explanations)",
                input_variables=["language", "task"]
            )

            test_prompt = PromptTemplate(
                template="Write a test for the following {language} code:\n{code}\n(return only the test code, no explanations)",
                input_variables=["language", "code"]
            )

            # Chain
            code_chain = LLMChain(llm=model, prompt=code_prompt, output_key="code")
            test_chain = LLMChain(llm=model, prompt=test_prompt, output_key="test")
            chain = SequentialChain(
                chains=[code_chain, test_chain],
                input_variables=["language", "task"],
                output_variables=["code", "test"]
            )

            # Execute and display result
            with st.spinner("Generating code and test..."):
                try:
                    result = chain({"language": language, "task": task})
                    col_code, col_test = st.columns(2)

                    with col_code:
                        st.markdown("###  Generated Code")
                        st.code(result["code"], language=language.lower())

                    with col_test:
                        st.markdown("###  Generated Test")
                        st.code(result["test"], language=language.lower())

                except Exception as e:
                    st.error(f" Error generating code: {str(e)}")
