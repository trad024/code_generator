import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse
import os

# Load environment variables
load_dotenv()
print("API Key:", os.environ.get("GOOGLE_API_KEY"))  # Debug print
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Rest of the script remains the same
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.environ.get("GOOGLE_API_KEY"))
parser = argparse.ArgumentParser(description="Generate code and tests using Gemini-Pro")
parser.add_argument("--task", default="sort a list of numbers", help="Task description")
parser.add_argument("--language", default="python", help="Programming language")
args = parser.parse_args()

code_prompt = PromptTemplate(
    template="Write a {language} code that will perform the following task: {task} (return only the code, no explanations)",
    input_variables=["language", "task"]
)

test_prompt = PromptTemplate(
    template="Write a test for the following {language} code:\n{code}\n(return only the test code, no explanations)",
    input_variables=["language", "code"]
)

code_chain = LLMChain(llm=model, prompt=code_prompt, output_key="code")
test_chain = LLMChain(llm=model, prompt=test_prompt, output_key="test")
chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["language", "task"],
    output_variables=["code", "test"]
)

try:
    result = chain({"language": args.language, "task": args.task})
    print("Generated Code:")
    print(result["code"])
    print("\nTest Code:")
    print(result["test"])
except Exception as e:
    print(f"Error: {str(e)}")