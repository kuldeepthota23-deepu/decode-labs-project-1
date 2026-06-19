# # Rule-Based AI Chatbot v1.0 - Created by [Thota Kuldeep]
responses = {
    "hello": "Hi there! How can I help you today?",
    "what is your name?": "I am a Rule-Based AI Chatbot created for DecodeLabs.",
    "how are you?": "I'm functioning perfectly!",
    "bye": "Goodbye! Have a great day."
}

print("Bot: Hello! Type 'exit' to stop.")

while True:
    user_input = input('You: ').lower().strip()
    
    if user_input == 'exit':
        print("Bot: Goodbye!")
        break
    
    # Intent Matching: Searching the Dictionary
    # .get() is safer because it provides a default if the key isn't found
    response = responses.get(user_input, "I'm not sure how to respond to that.")
    print(f"Bot: {response}")