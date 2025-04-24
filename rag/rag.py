from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
import os
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')

_GLOBAL_INDEX = None

def get_index():
    global _GLOBAL_INDEX
    
    if _GLOBAL_INDEX is None:
        Settings.llm = Groq(model="llama-3.3-70b-versatile", api_key=os.getenv('GROQ_API_KEY'))
        Settings.embed_model = HuggingFaceEmbedding(model_name='BAAI/bge-small-en-v1.5')
        embed_model = HuggingFaceEmbedding(model_name='BAAI/bge-small-en-v1.5')
        storage_dir = f"./chromaDB"
        db = chromadb.PersistentClient(path=storage_dir)
        chroma_collection = db.get_or_create_collection("mcp-rag")
        
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        _GLOBAL_INDEX = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)
    
    return _GLOBAL_INDEX