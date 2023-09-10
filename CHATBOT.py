#CHATBOTTASK1

import re

def simple_chatbot(user_input):
    if re.search(r'\bhello\b', user_input, re.I):
        return "Hello! How can I help you?"
    elif re.search(r'\bwho are you\b', user_input, re.I):
        return "I'm  a chatbot, and  I'm here to assist you!"
    elif re.search(r'\bWho is your boss?\b', user_input, re.I):
        return "Abdullah Hashim, is my boss !"
    elif re.search(r'\bWhat can you do here?\b', user_input, re.I):
         return "I'm  a chatbot, and  I'm here to assist you!"
    elif re.search(r'\bbye\b', user_input, re.I):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
