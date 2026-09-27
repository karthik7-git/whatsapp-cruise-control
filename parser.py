import re
import os

def parse_whatsapp_chat(file_path):
    """
    Parses a WhatsApp chat export file into structured messages:
    [Timestamp, Sender, Message]
    """
    # Standard WhatsApp export regex pattern
    pattern = r'^\[?(\d{1,2}/\d{1,2}/\d{2,4},?\s+\d{1,2}:\d{2}(?::\d{2})?(?:\s+[APap][Mm])?)\]?\s+([^:]+):\s+(.*)$'
    
    structured_data = []
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at {file_path}")
        return structured_data

    print(f"📂 Reading file from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        line_count = 0
        match_count = 0
        for line in f:
            line_count += 1
            match = re.match(pattern, line.strip())
            if match:
                match_count += 1
                timestamp, sender, message = match.groups()
                if "media omitted" not in message.lower():
                    structured_data.append({
                        "timestamp": timestamp,
                        "sender": sender.strip(),
                        "message": message.strip()
                    })
                    
    print(f"🔍 Scanned {line_count} total lines, matched {match_count} message lines.")
    return structured_data

if __name__ == "__main__":
    # Make sure your file name matches exactly
    chat_file = "data/raw_chats/chat_export.txt"
    parsed_messages = parse_whatsapp_chat(chat_file)
    
    print(f"✅ Successfully parsed {len(parsed_messages)} valid messages!")
    
    if len(parsed_messages) > 0:
        print("\n--- Preview of First 3 Messages ---")
        for m in parsed_messages[:3]:
            print(f"[{m['timestamp']}] {m['sender']}: {m['message']}")
    else:
        print("⚠️ Warning: 0 messages parsed. Your chat text format might slightly differ from standard WhatsApp timestamps (e.g., [DD/MM/YY, HH:MM:SS]). Let me know and we can tweak the regex pattern!")