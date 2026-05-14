import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm good!", "Doing great!", "All fine!"]
}

def chatbot():
    while True:
        user = input("You: ").lower()

        if user in responses:
            print("Bot:", random.choice(responses[user]))
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Try asking something else.")

chatbot()