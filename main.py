import datetime

print("Welcome to the Chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hello! How can I assist you today?")
    elif user_input == "how are you":
        print("Bot: I'm doing great! How about you?")
    elif user_input == "what is your name":
        print("Bot: My name is JARVIS.")
    elif user_input == "what can you do":
        print("Bot: I can chat with you, answer simple questions, and keep you company!")
    elif user_input == "greet me":
        hour = datetime.datetime.now().hour
        if hour < 12:
            print("Bot: Good morning!")
        elif hour < 18:
            print("Bot: Good afternoon!")
        else:
            print("Bot: Good evening!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
