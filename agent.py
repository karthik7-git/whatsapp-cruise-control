import os
import chromadb
from router import should_reply

def retrieve_similar_messages(query_text, n_results=3):
    """
    Retrieves the most semantically similar messages sent by you from ChromaDB.
    """
    client = chromadb.PersistentClient(path="./chroma_db")
    try:
        collection = client.get_collection(name="whatsapp_rag_collection")
    except Exception:
        return []
    
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    # Extract the documents/messages
    if results and 'documents' in results and len(results['documents']) > 0:
        return results['documents'][0]
    return []

def generate_persona_response(sender, incoming_message):
    """
    Orchestrates the pipeline: Router -> RAG Retrieval -> Persona Generation Prompt
    """
    # 1. Check router rules
    approved, reason = should_reply(sender, incoming_message)
    if not approved:
        return f"🚫 [{reason}]"

    # 2. Retrieve past context via RAG
    past_examples = retrieve_similar_messages(incoming_message, n_results=3)
    
    # 3. Construct prompt context
    context_str = "\n".join([f"- {msg}" for msg in past_examples]) if past_examples else "No specific past context found."

    # 4. Generate the final prompt combining your persona rules + retrieved context
    prompt = f"""
You are an AI assistant replying on WhatsApp on behalf of Ravipati Karthik.
You must reply in Karthik's exact texting style (lowercase preference, natural Hinglish slang if applicable, short and casual).

Incoming Message from {sender}: "{incoming_message}"

Here are examples of how Karthik has historically replied to similar messages:
{context_str}

Draft a short, authentic reply as Karthik would write it. Do not include any meta-commentary or prefix.
"""
    
    # For now, let's output the assembled prompt and RAG context to test your full pipeline!
    return f"\n✨ [RAG Context Retrieved]:\n{context_str}\n\n🤖 [Generated Response Ready for WhatsApp Pipeline]"

if __name__ == "__main__":
    # Test the full pipeline with a mock incoming message
    test_sender = "Dileep"
    test_msg = "Bhai kal match hai kya?"
    
    print(f"Incoming from {test_sender}: '{test_msg}'")
    print(generate_persona_response(test_sender, test_msg))