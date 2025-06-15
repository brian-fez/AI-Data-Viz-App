### llm_chat.py
import re
from typing import Optional, List, Tuple
from langchain_community.llms import Ollama
import streamlit as st
from docker_executor import code_interpret_docker

pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)

def match_code_blocks(llm_response: str) -> str:
    match = pattern.search(llm_response)
    return match.group(1) if match else ""

def chat_with_llm(user_message: str, dataset_path: str, error_handler, max_retries: int = 3) -> Tuple[Optional[List[str]], str]:
    llm = Ollama(model="deepseek-coder:6.7b", temperature=0.2)

    prompt = f"""You are a Python data scientist and data visualization expert.
You have a CSV dataset at path '/data/dataset.csv'. Use this path in your code.
Perform analysis directly on that dataset. Never create dummy data or assume columns not present
in the dataset. Answer the user's query, and include any Python code in triple backticks like:
```python
# code here
```
If your answer involves plotting (e.g. with matplotlib or plotly), you must:
1. Save the plot to '/tmp/chart.png'
2. Encode it to base64
3. Print only the base64-encoded string. Do not include any data URI prefixes (e.g., 'data:image/jpeg;base64,')
User query: {user_message}"""

    for attempt in range(max_retries):
        response = llm(prompt)
        python_code = match_code_blocks(response)

        if not python_code:
            return None, response

        code_result = code_interpret_docker(python_code, dataset_path, error_handler)

        if code_result is not None:
            return code_result, response

        error_message = f"Your last code caused an error during execution. Please fix it.\n\n" \
                f"The error was:\n```\n{st.session_state.get('last_error', 'Unknown error')}\n```"
        prompt = f"{response}\n\n{error_message}\n\nPlease provide corrected Python code."

    return None, f"Failed after {max_retries} attempts. Last LLM response:\n\n{response}"