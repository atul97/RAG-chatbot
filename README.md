

# RAG Chatbot with LangChain, GROQ LLM, Google Gemini API (for Embeddings), FAISS, and Streamlit

## Overview

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that combines document retrieval, semantic search, and generative AI to provide highly accurate and context-aware responses to user queries. The chatbot leverages **LangChain**, **GROQ LLM**, **Google Gemini API (for embeddings)**, **FAISS**, and **Streamlit** for seamless interaction and efficiency.

---

## Features

- **LangChain Integration**: For orchestrating retrieval pipelines and chaining various components like embeddings, search, and generative models.
- **Google Gemini API for Embedding**: Utilizes the Gemini API key to generate embeddings for semantic search.
- **GROQ LLM for Response Generation**: GROQ is employed for generating human-like responses based on retrieved document context.
- **FAISS**: Efficient indexing and search for embedding vectors to retrieve the most relevant documents.
- **Streamlit Interface**: A user-friendly, web-based UI for interactive chatbot functionality.

---

## Requirements

To run this project, ensure you have the necessary dependencies listed in the `requirements.txt` file.

### Install the dependencies

```bash
pip install -r requirements.txt
```

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/atul97/RAG-chatbot.git 
   cd rag-chatbot
   ```

2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Place your RAG documents**:
   - Add your documents to the **`documents/`** folder in the root directory. These will be processed for embedding generation and document retrieval.

4. **Configure the `.env` file**:
   - Rename `.env.example` to `.env` and provide your **Google Gemini API key** for embedding generation and **GROQ token** for LLM-based response generation.

   Example `.env` file:

   ```dotenv
   # .env

   GROQ_API_KEY = your-groq-token
   GOOGLE_API_KEY = your-gemini-api-key
   ```

   Replace `your-gemini-api-key` with your Gemini API key (used only for embedding generation) and `your-groq-token` with your GROQ token for LLM responses.

---

## Running the Application

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Access the chatbot**:
   - After running the app, navigate to `http://localhost:8501` in your web browser.
   - Enter a query or message, and the chatbot will process the input using document retrieval and generative AI.

---

## How It Works

1. **Document Embedding**:  
   - Documents in the **`documents/`** folder are processed using the **Google Gemini API key** to generate embeddings. These embeddings capture the semantic meaning of the documents for better search and retrieval.

2. **FAISS Indexing**:  
   - The embeddings are indexed using **FAISS**, enabling efficient vector search to retrieve the most relevant documents quickly.

3. **Document Retrieval**:  
   - Based on user queries, LangChain retrieves the most relevant documents using FAISS. The embeddings are matched against the query for semantic similarity.

4. **GROQ LLM Response Generation**:  
   - The retrieved document context and query are passed to the **GROQ LLM**, which generates human-like responses. GROQ ensures high-quality generative outputs tailored to the user’s intent and the context of the retrieved documents.

5. **Streamlit Interaction**:  
   - The chatbot interface is built with **Streamlit**, allowing users to interact with the chatbot through a simple and intuitive web app.

---

## Contributions

We welcome contributions! Feel free to fork the repository, submit pull requests, and suggest improvements to enhance the project further.

---

## Acknowledgements

- **LangChain**: For simplifying the orchestration of retrieval and generative pipelines.
- **FAISS**: For fast and scalable vector search to retrieve document embeddings.
- **Google Gemini API**: For generating high-quality embeddings for semantic search.
- **GROQ LLM**: For generating accurate and context-aware conversational responses.
- **Streamlit**: For providing a user-friendly interface for chatbot interaction.

