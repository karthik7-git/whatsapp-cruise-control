def should_reply(sender, message_text):
    """
    Evaluates incoming messages using hard rules and logic
    before deciding to invoke the RAG generator.
    """
    # Rule 1: Ignore system messages or empty inputs
    if not message_text or "media omitted" in message_text.lower():
        return False, "Ignored: Empty or media message"
        
    # Rule 2: Ignore automated keywords or OTPs (Safety Filter)
    spam_keywords = ["otp", "verification code", "dear customer", "congratulations you won"]
    if any(keyword in message_text.lower() for keyword in spam_keywords):
        return False, "Ignored: Detected OTP or spam keyword"

    # Rule 3: Engage for normal conversational queries
    return True, "Approved: Proceed to RAG generation"

if __name__ == "__main__":
    # Quick test cases
    test_cases = [
        ("Nihaaaaa", "Bhai kal match hai kya?"),
        ("Unknown", "Your OTP is 489210, do not share."),
        ("Nihaaaaa", "👍")
    ]
    
    for sender, msg in test_cases:
        approved, reason = should_reply(sender, msg)
        print(f"[{sender}] '{msg}' -> Status: {reason}")