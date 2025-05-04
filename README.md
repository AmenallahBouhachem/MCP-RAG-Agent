# MCP-RAG-Agent

## 🌟 Overview

**MCP-RAG-Agent** is a cutting-edge AI-powered medical assistant. It allows users to input their symptoms and provides responses using the Retrieval-Augmented Generation (RAG) tool. If the RAG tool cannot find a suitable response, the system seamlessly performs an internet search to fetch accurate and real-time information.

This project is designed to assist users in understanding medical conditions and symptoms, making it a valuable tool for healthcare professionals and individuals alike.

---

## 📂 Project Structure

```
MCP-RAG-Agent/
├── chromaDB/                            # Vector database
├── data/                                # Medical symptoms and diseases data
├── Chroma_DB_Generation.py              # Script to generate the vector database
├── rag.py                               # Script to load the index of the vector database
├── server.py                            # Script to create the MCP server
├── main.py                              # Script to run the Agent
├── requirements.txt                     # Packages to install
└── README.md                            # Project overview
```

---

## 🛠️ Features

- **Medical Symptom Analysis**: Users can input symptoms to receive AI-generated responses.
- **RAG Tool**: Retrieves relevant medical information from a vector database.
- **Web Search Tool**: Fetches real-time medical information from the internet when needed.
- **ChromaDB**: Utilizes ChromaDB for efficient vector storage and retrieval.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MCP-RAG-Agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MCP-RAG-Agent/rag
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

---

## 🚀 Usage

1. **Start the MCP Server**:
   Run the `main.py` script to start the MCP server:

   ```bash
   python main.py
   ```
2. **Interact with the Agent**:

   - Input your symptoms into the system.
   - The agent will respond using the RAG tool or perform an internet search if necessary.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 📬 Contact

For inquiries or support, please contact:

- **Email**: amenallah8bouhachem@gmail.com
- **GitHub**: [AmenallahBouhachem](https://github.com/AmenallahBouhachem)
