from agent import generate_persona_response

def start_cruise_control():
    print("=" * 60)
    print("🚀 WHATSAPP CRUISE CONTROL: AGENT CONSOLE IS LIVE")
    print("Type an incoming message to test your AI ghostwriter.")
    print("Type 'exit' to quit.")
    print("=" * 60)

    # Let's default test sender name
    sender = "Karthik"

    while True:
        try:
            incoming = input(f"\n📥 Simulate incoming message from {sender}: ")
            if incoming.strip().lower() == 'exit':
                print("Shutting down Cruise Control. Safe travels! 👋")
                break
            
            if not incoming.strip():
                continue

            # Run through Router -> RAG Retrieval -> Persona Generation
            response = generate_persona_response(sender, incoming)
            print(response)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    start_cruise_control()