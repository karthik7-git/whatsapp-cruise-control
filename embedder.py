import os
import chromadb
from parser import parse_whatsapp_chat

def create_vector_db():
    # 1. Parse the chat
    chat_file = "data/raw_chats/chat_export.txt"
    messages = parse_whatsapp_chat(chat_file)
    
    if not messages:
        print("No messages found to embed!")
        return

    print(f"Loaded {len(messages)} messages. Initializing ChromaDB...")

    # 2. Initialize Chroma client (persistent storage locally)
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Create or get collection
    collection = client.get_or_create_collection(name="whatsapp_rag_collection")

    # 3. Prepare data for ChromaDB
    documents = []
    metadatas = []
    ids = []

    for i, m in enumerate(messages):
        # Filter for messages sent by you. 
        # NOTE: Change 'You' below to whatever your sender name appears as in chat_export.txt if it differs!
        # Check for your exact name from the parser output
        if m['sender'].strip() == "- Karthik 👑":  
            documents.append(m['message'])
            metadatas.append({"timestamp": m['timestamp'], "sender": m['sender']})
            ids.append(f"msg_{i}")

    if not documents:
        print("⚠️ Warning: 0 messages found sent by 'You'. Check your exact sender name in chat_export.txt!")
        return

    # 4. Add to collection
    print(f"Embedding {len(documents)} messages sent by you...")
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print("🚀 Vector database successfully created and stored in './chroma_db'!")

if __name__ == "__main__":
    create_vector_db()