# Azure RAG Demo (Simulated)

This project simulates a Retrieval-Augmented Generation (RAG) pipeline similar to what you'd build using **Azure AI Search** and **Azure OpenAI**. It uses OpenAI’s embedding API and GPT model to retrieve relevant context and generate answers, simulating how AI agents in Azure might function.

---

## 🔧 What It Does

- Loads content from `documents.txt`
- Generates embeddings using `text-embedding-ada-002` (OpenAI)
- Stores embeddings in a FAISS index
- Accepts user questions, retrieves relevant text chunks, and sends them to `gpt-3.5-turbo` for a response

---

## 📦 Technologies Used

- Python
- OpenAI API (Embeddings + GPT chat)
- FAISS (Vector similarity search)
- Minimal local resources – avoids transformer model loading

---

## 🚀 How to Set Up and Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/azure-rag-demo.git
cd azure-rag-demo
```

### 2. Add Your Knowledge Base

Create or edit the file `documents.txt` in the project root.  
Each line should contain a standalone fact, paragraph, or document snippet.

**Example `documents.txt`:**
```
Azure AI Search is a cloud-based enterprise search engine.
Cosmos DB is a globally distributed NoSQL database.
Azure AI Foundry helps orchestrate LLM workflows using Azure OpenAI and Search.
```

### 3. Set Your OpenAI API Key

In PowerShell:
```bash
$env:OPENAI_API_KEY="sk-..."   # Replace with your actual OpenAI key
```

> 💡 Never hardcode your API key in `main.py` if pushing code to GitHub.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```
openai
faiss-cpu
```

### 5. Run the App

```bash
python main.py
```

You’ll see:
```
Ask a question (or type 'exit'):
```

Example input:
```
What is Cosmos DB?
```

---

## 📁 Files Overview

| File             | Description                        |
|------------------|------------------------------------|
| `main.py`        | Main pipeline script               |
| `documents.txt`  | Knowledge base for retrieval       |
| `requirements.txt` | Python dependencies              |
| `README.md`      | Setup and usage instructions       |
