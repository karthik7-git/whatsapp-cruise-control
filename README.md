# 🚀 WhatsApp on Cruise Control
### Hands-Free Replies by an AI Agent Using RAG

> *Train an AI agent on your exact chat history so it replies in your personal style — your phrasing, your Hinglish slang, your emojis, and your natural tone.*

---

## 🧐 What Is This Project?
This isn't a generic chatbot wearing your name[cite: 1]. This is a **retrieval-grounded persona agent** built from scratch over four weeks[cite: 1]. 

When an incoming message arrives, your agent:
1. **Evaluates** whether it warrants a reply (filtering out OTPs, spam, and system notifications)[cite: 1].
2. **Retrieves** how you've historically talked about similar topics using semantic vector search (RAG)[cite: 1].
3. **Generates** an authentic response matching your precise texting style, capitalization habits, and regional slang[cite: 1].

---

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.10+
- **Vector Database:** ChromaDB (Local, zero-budget vector storage)
- **Embeddings:** Hugging Face Sentence Transformers (`all-MiniLM-L6-v2`)
- **Parsing & Regex:** Custom Python chat log cleaners
- **Automation & Bridge:** PyAutoGUI & WhatsApp Web integration

---

## 🗺️ The 4-Week Roadmap
* **Week 1 — The Ghostwriter:** Defined core persona rules, identity bounds, and style guidelines (`persona.md`).
* **Week 2 — The Curator:** Parsed nearly 2,000 raw WhatsApp export lines and built a persistent local ChromaDB vector store (`parser.py`, `embedder.py`).
* **Week 3 — The Router:** Built a hard-filter decision engine to catch spam and prioritize real conversations (`router.py`).
* **Week 4 — The Puppetmaster:** Tied RAG retrieval, persona injection, and live dispatch together (`agent.py`, `run_agent.py`).

---

## 📂 Project Structure
```text
whatsapp-ai-agent/
│
├── data/
│   └── raw_chats/         # Place your exported WhatsApp .txt chat logs here
├── chroma_db/             # Local persistent vector database storage
├── persona.md             # Your custom persona prompt and voice rules
├── parser.py              # WhatsApp chat export parser
├── embedder.py            # Vector embedding generator (ChromaDB)
├── router.py              # Rule-based decision engine
├── agent.py               # RAG retriever & persona prompt orchestrator
└── run_agent.py           # Interactive local terminal agent console
🚀 Getting Started Locally
1. Clone the Repository
Bash
git clone [https://github.com/your-username/whatsapp-cruise-control.git](https://github.com/your-username/whatsapp-cruise-control.git)
cd whatsapp-cruise-control
2. Install Dependencies
Bash
pip install chromadb sentence-transformers pyautogui pywhatkit
3. Add Your Chat Export
Export your chat from WhatsApp (More > Export chat > Without Media)[cite: 1].

Place the extracted .txt file inside data/raw_chats/.

Update the file path in parser.py and your sender name filter in embedder.py.

4. Build Your Vector Database
Run the embedder to vectorize your personal chat history:

Bash
python embedder.py
5. Launch the Agent Console
Run the interactive simulation loop to test your RAG persona agent:

Bash
python run_agent.py
💡 Example Simulation
Plaintext
============================================================
🚀 WHATSAPP CRUISE CONTROL: AGENT CONSOLE IS LIVE
Type an incoming message to test your AI ghostwriter.
============================================================

📥 Simulate incoming message from Dileep: Bhai kal match hai kya?
✨ [RAG Context Retrieved]:
- Hai
- Khana hogaya aapka..?

🤖 [Generated Response Ready for WhatsApp Pipeline]
📜 License
This project is open-source and built for educational and demonstration purposes.


---

### How to push this to GitHub:
If you want to push this straight to your GitHub repository from your terminal, run these commands:
```cmd
git init
git add .
git commit -m "Initial commit: WhatsApp Cruise Control RAG agent"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/whatsapp-cruise-control.git
git push -u origin main
