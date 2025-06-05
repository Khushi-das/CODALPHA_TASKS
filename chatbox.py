import random

# Basic chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a program, but I'm doing fine!", "All good here!", "Running smoothly!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "what's your name?":["i am a virtual chatbox i don't have name"],
    "what is python":["python is a widely used programing language"],
    "thankyou":["you are welcome feel free to ask any other queiries"],
    "default": ["Sorry, I didn't understand that.", "Could you rephrase?", "I'm not sure what you mean."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if 'bye' in user_input.lower():
        print("ChatBot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("ChatBot:", response)