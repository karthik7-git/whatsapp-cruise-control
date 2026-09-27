import time
import pywhatkit
import pyautogui
from agent import generate_persona_response

def send_live_whatsapp_reply(phone_number, sender_name, incoming_message):
    print(f"🔄 Processing message from {sender_name}...")
    ai_response = generate_persona_response(sender_name, incoming_message)
    print(f"🤖 Generated Persona Text: {ai_response}")
    
    print(f"🚀 Launching WhatsApp Web to send to {phone_number}...")
    
    # 1. Open chat via pywhatkit (gives it 15 seconds to load up)
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone_number, 
        message=ai_response, 
        wait_time=15,  
        tab_close=False 
    )
    
    # 2. Explicitly force an Enter key press using PyAutoGUI to send it
    time.sleep(3)
    pyautogui.press('enter')
    print("✅ Triggered send key successfully!")

if __name__ == "__main__":
    test_phone = "+91XXXXXXXXXX"  # Replace with your test number
    test_sender = "Karthik"
    test_incoming = "Bhai kal match hai kya?"
    
    send_live_whatsapp_reply(test_phone, test_sender, test_incoming)

    