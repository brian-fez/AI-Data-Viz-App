# 📊 AI Data Visualization Agent

This project is an AI-powered data visualization assistant built with **LangChain**, **Ollama**, **Docker**, and **Streamlit**. It allows you to upload a CSV dataset, ask natural language questions about it, and receive visual or tabular insights with Python code execution in a secure, sandboxed environment.

---

## 🚀 Features

- 🧠 **LLM-powered analysis** using [Deepseek Coder]([https://huggingface.co/deepseek-ai/deepseek-coder](https://ollama.com/library/deepseek-coder))
- 📈 **Dynamic visualizations** via `matplotlib` or `plotly`
- 🐳 **Secure Python execution** in a Docker sandbox (no local code is run unsafely)
- 🔍 **Natural language interface** for querying CSV datasets
- 🧾 **Base64 image rendering** for charts within Streamlit

---

## 🗂️ Project Structure

```
.
├── app.py                # Streamlit frontend
├── llm_chat.py           # Handles prompting and parsing LLM responses
├── docker_executor.py    # Executes LLM-generated Python in Docker
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and usage
```
---

## ⚙️ Prerequisites

- Python 3.9+
- [Docker](https://docs.docker.com/get-docker/)
- [Ollama](https://ollama.com) with `deepseek-coder` model pulled:
  ```bash
  ollama pull deepseek-coder:6.7b
  ```

---

## 🛠️ Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brian_fez/AI-Data-Viz-App.git
   cd AI-Data-Viz-App
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build Docker sandbox image (if not already built):**
   ```bash
   docker build -t python-sandbox ./docker
   ```

---

## ▶️ Running the App

Start the Streamlit app:
```bash
streamlit run app.py
```
---

## 📁 Example Workflow

1. Upload a CSV file.
2. Ask a question like:
   > “Can you show a bar chart comparing average sales by year?”
3. The app:
   - Sends your query and dataset to the LLM
   - Receives and parses Python code
   - Runs it inside Docker
   - Displays the result (chart or text)

---

## 🧱 Docker Notes

The Docker container mounts:
- `/data/dataset.csv` as the uploaded CSV (read-only)
- `/app/code.py` as the generated Python script

It executes the code safely in isolation and returns the output (e.g., base64 chart).

---

## 📌 Limitations

- The LLM will only generate code based on columns present in your dataset.
- Execution is limited to 30 seconds per run to avoid long/hanging scripts.

---

## 📄 License

MIT License © 2025 brian_fez

---

## 💡 Future Improvements

- Support for multi-turn chat with history
- Export charts and code
- Multiple plot formats (e.g., SVG)
- Add tests and LLM response validation

---

```
