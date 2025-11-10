print("Hi! I am Chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")
    elif "your name" in user_input:
        print("Bot: I am a simple CLI chatbot.")
    elif "weather" in user_input:
        print("Bot: Sorry, I can't check the weather right now.")
    elif "bye" in user_input:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
