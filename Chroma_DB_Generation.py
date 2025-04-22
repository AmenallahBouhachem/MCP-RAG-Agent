import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from dotenv import load_dotenv
import chromadb
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

load_dotenv()

os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
Settings.embed_model = HuggingFaceEmbedding(
    model_name='BAAI/bge-small-en-v1.5')


def chroma_db_generation(input_path: str):
    db_path = './chromaDB'
    os.makedirs(db_path, exist_ok=True)
    reader = SimpleDirectoryReader(input_dir=input_path)
    data = reader.load_data()
    db = chromadb.PersistentClient(path=db_path)
    chroma_collection = db.get_or_create_collection('mcp-rag')
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(data,storage_context=storage_context,show_progress=True)
    print("Chroma DB generation process completed!")


chroma_db_generation(input_path='./data')