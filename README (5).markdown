# Code Generation Project

## Overview
This project is a Python-based code generator that leverages the Google Gemini-Pro API to automatically generate code and corresponding test cases for various programming tasks. It provides two interfaces:
- A command-line tool (`code_generator.py`) for generating code and tests via terminal commands.
- A web-based interface (`code_generator_ui.py`) built with Streamlit for user-friendly interaction.

The project uses LangChain to chain prompts for code and test generation, and it supports multiple programming languages, including Python, Java, JavaScript, and more.

## Features
- Generate functional code for tasks like "sort a list of numbers" or "reverse a string."
- Automatically create test cases (e.g., using `unittest` for Python) to validate the generated code.
- Support for multiple programming languages via a dropdown in the web interface.
- Error handling for invalid inputs and API issues.
- Debug logging to verify environment setup (e.g., API key loading).

## Requirements
- **Python**: Version 3.8 or higher (download from [python.org](https://www.python.org/downloads/)).
- **Google API Key**: Obtain a key for the Google Generative AI API from [Google Cloud Console](https://console.cloud.google.com/).
- **Dependencies**:
  - `google-generativeai==0.7.2`
  - `langchain==0.3.0`
  - `langchain-google-genai==1.0.10`
  - `python-dotenv`
  - `streamlit==1.38.0`
- **Operating System**: Windows, macOS, or Linux (instructions assume Windows).

## Setup Instructions
1. **Clone or Download the Project**:
   - Download the project files to a local directory (e.g., `C:\code_generation_project`).

2. **Set Up a Virtual Environment**:
   - Open a terminal in the project directory (e.g., in VS Code: `Terminal > New Terminal`).
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - Windows (PowerShell):
       ```powershell
       .\venv\Scripts\activate
       ```
       If you get a "scripts disabled" error, set the PowerShell execution policy:
       ```powershell
       Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
       ```
     - Mac/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - In the activated virtual environment (`(venv)` prompt), run:
     ```bash
     pip install google-generativeai==0.7.2 langchain==0.3.0 langchain-google-genai==1.0.10 python-dotenv streamlit==1.38.0
     ```

4. **Configure the Google API Key**:
   - Create a file named `.env` in the project root (`C:\code_generation_project`).
   - Add your Google API key:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```
     Replace `your_api_key_here` with your actual key from Google Cloud Console.
   - Ensure the `.env` file has no extra spaces or quotes.

5. **Verify Setup**:
   - Run the command-line script to check if the API key loads:
     ```bash
     python code_generator.py --task "sort a list of numbers" --language python
     ```
   - Expected output includes debug prints (e.g., `API Key: <your_key>`) and generated code/tests.

## Usage
### Command-Line Tool (`code_generator.py`)
- Generate code and tests for a task:
  ```bash
  python code_generator.py --task "sort a list of numbers" --language python
  ```
- Example output:
  ```
  Current Working Directory: C:\code_generation_project
  Does .env exist? True
  API Key: AIzaSyYourKey
  Generated Code:
  def sort_list(numbers):
      return sorted(numbers)

  Test Code:
  import unittest
  class TestSortList(unittest.TestCase):
      def test_empty_list(self):
          self.assertEqual(sort_list([]), [])
      ...
  ```

### Web Interface (`code_generator_ui.py`)
- Run the Streamlit app:
  ```bash
  streamlit run code_generator_ui.py
  ```
- Open `http://localhost:8501` in a browser.
- Select a language (e.g., Python), enter a task (e.g., "sort a list of numbers"), and click "Generate Code."
- The interface displays the generated code and tests with syntax highlighting.

## Troubleshooting
- **Streamlit Command Not Found**:
  - Ensure the virtual environment is activated (`(venv)` in prompt).
  - Reinstall Streamlit: `pip install streamlit==1.38.0`.
- **API Key: None**:
  - Verify `.env` exists in `C:\code_generation_project` and contains `GOOGLE_API_KEY`.
  - Check file name (not `.env.txt`) and formatting (no extra spaces/quotes).
- **PowerShell Scripts Disabled**:
  - Run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.
- **Invalid API Key**:
  - Regenerate the key in Google Cloud Console and update `.env`.
- **Port Conflict**:
  - If `localhost:8501` is in use, run: `streamlit run code_generator_ui.py --server.port 8502`.

## License
MIT License (or specify your preferred license).