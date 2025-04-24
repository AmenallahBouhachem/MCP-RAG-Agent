# MCP-RAG-Agent

## 🚀 Overview

**MCP-RAG-Agent** is an advanced implementation of a Model Context Protocol (MCP) server. It integrates two powerful tools:

1. **RAG Tool**: A Retrieval-Augmented Generation tool designed to handle machine learning content queries by retrieving the most relevant documents from a vector database.
2. **Web Search Tool**: A tool that performs internet searches to fetch information in response to user queries.

This project leverages MCP to enable seamless interaction between AI systems and external tools, making it ideal for developers, researchers, and enthusiasts looking to build context-aware AI workflows.

---

## 📂 Project Structure

```
MCP-RAG-Agent/
├── chromaDB/                            # Vector database
├── data/                                # Text data
├── Chroma_DB_Generation.py              # Script to generate the vector database
├── rag.py                               # Script to load the index of the vector database
├── server.py                            # Script to create the MCP server
├── requirements.txt                     # Packages to install
└── README.md                            # Project overview
```

---

## 🛠️ Features

- **MCP Integration**: Implements the Model Context Protocol for standardized AI-tool interactions.
- **RAG Tool**: Retrieves relevant machine learning documents from a vector database.
- **Web Search Tool**: Fetches real-time information from the internet.
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
   Run the `server.py` script to start the MCP server:

   ```bash
   go to mcp.json file and press start server button
   ```
2. **Use the Tools**:

   - **RAG Tool**: Query the vector database for machine learning content.
   - **Web Search Tool**: Perform internet searches for real-time information.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 📬 Contact

For inquiries or support, please contact:

- **Email**: amenallah8bouhachem@gmail.com
- **GitHub**: [AmenallahBouhachem](https://github.com/AmenallahBouhachem)
