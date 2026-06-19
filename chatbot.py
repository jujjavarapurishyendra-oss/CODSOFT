print("Welcome to my Chatbot! ")
while True:
    user = input("You: ").lower()
    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thanl you!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    elif user == "what is your name":
    print("Bot: My name is AI Assistant.")

elif user == "help":
    print("Bot: You can ask me greetings and simple questions.")

elif user == "thank you":
    print("Bot: You're welcome!")
    else:
        print("Bot: Sorry, I don't understand.")