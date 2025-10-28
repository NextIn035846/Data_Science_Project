
# 🐼 Pandas Data Analyst AI

This AI agent analyzes your dataset on the fly, making data analysis fast, conversational, and accessible to everyone.

## 🚀 The Problem

Getting quick insights from a dataset often means writing repetitive, boilerplate Pandas code just to filter, group, or plot data. This slows down analysis and makes it inaccessible to those who aren't code-savvy.

I built the Pandas Data Analyst AI to solve that.

## Demo 

https://github.com/user-attachments/assets/1042adf9-5497-4d81-98d1-8f1df0c1fc6d


## ✨ Features

It’s simple:
* **Upload your CSV/Excel file.**
* **Ask questions in natural language** (e.g., "What's the average sales by region?" or "Show me a bar chart of the top 10 products by profit").
* **Get answers as data tables or interactive charts.**

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Core:** Pandas
* **LLM:** [Your LLM - e.g., OpenAI, Gemini, Groq, Ollama]
* **Agent Framework:** [LangChain]

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Prerequisites

* Python 3.9+
* An API key for [Your LLM Service - e.g., OpenAI].

### 2. Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/NextIn035846/Data_Science_Project.git
    cd Data_Science_Project
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### 3. Setup Environment

1.  Create a `.env` file in the root directory.
2.  Add your API key:

    ```env
    # Example for OpenAI
    OPENAI_API_KEY="sk-..."
    ```

### 4. Run the App

1.  Launch the Streamlit app:
    ```sh
    streamlit run App.py
    ```
2.  Open your browser to `http://localhost:8501` and start analyzing!

## 🧠 How It Works

This agent uses an LLM to intelligently convert your natural language questions into executable Pandas code.

1.  **Upload:** The app loads your CSV or Excel file into a Pandas DataFrame.
2.  **Query:** You ask a question, like "What are the total sales?"
3.  **Generate:** The LLM generates the Python/Pandas code required to answer that question (e.g., `df['sales'].sum()`).
4.  **Execute:** The generated code is safely executed against the DataFrame.
5.  **Display:** The result (whether it's a number, a table, or a chart) is displayed back to you in the Streamlit UI.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/NextIn035846/Data_Science_Project.git/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Highlights
- Upload CSV / Excel and interact with your dataset conversationally
- Natural-language queries converted to safe pandas operations
- Results returned as pandas DataFrame and optional interactive charts (Plotly / Altair)
- Quick visualizations: bar, line, scatter, histogram, correlation heatmap
- Export results back to CSV / Excel or save charts as images

