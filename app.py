### app.py
import base64
import tempfile
from io import BytesIO
from PIL import Image

import pandas as pd
import streamlit as st

from llm_chat import chat_with_llm

def handle_error(msg):
    st.session_state["last_error"] = msg

def main():
    st.title("📊 AI Data Visualization Agent (LangChain + Ollama + Docker Sandbox)")
    st.write("Upload your dataset and ask questions about it!")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        show_full = st.checkbox("Show full dataset")
        if show_full:
            st.dataframe(df)
        else:
            st.write("Preview (first 5 rows):")
            st.dataframe(df.head())

        query = st.text_area(
            "What would you like to know about your data?",
            "Can you compare the average cost for two people between different categories?"
        )

        if st.button("Analyze"):
            with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp.flush()

                try:
                    code_results, llm_response = chat_with_llm(query, tmp.name, handle_error)

                    st.subheader("AI Response")
                    st.write(llm_response)

                    if code_results:
                        st.subheader("Code Execution Output")
                        for result in code_results:
                            if isinstance(result, str):
                                try:
                                    img_data = base64.b64decode(result.strip())
                                    image = Image.open(BytesIO(img_data))
                                    st.image(image, caption="Generated Visualization", use_container_width=True)
                                except Exception:
                                    st.text(result)
                            else:
                                st.write(result)
                    else:
                        st.warning("No executable Python code found in the AI response.")

                except Exception as e:
                    st.error(f"Error during execution: {e}")

if __name__ == "__main__":
    main()