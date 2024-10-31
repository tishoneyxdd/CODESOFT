import re
import random

greetings=["hello", "hi", "hey", "greetings", "what's up"]
goodbyes=["goodbye", "bye", "see you later", "quit","exit","end","close","stop"]
feeling_questions=["how are you", "how are you doing", "how are you feeling"]
help_keywords=["help", "support", "assist", "aid", "guidance"]
weather_keywords = ["weather", "temperature", "forecast"]
identity_questions = ["who are you", "what are you", "introduce yourself"]
special_easter=["who made you","who created you"]

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Greeting
    if any(greeting in user_input for greeting in greetings):
        return random.choice([
            "Hello! How can I assist you today?", 
            "Hi there! What's on your mind?", 
            "Hey! How can I help you?"
        ])
    
    # Goodbye
    elif any(goodbye in user_input for goodbye in goodbyes):
        return random.choice([
            "Goodbye! Have a great day ahead!", 
            "See you later! Take care!", 
            "Bye! Feel free to come back if you have more questions!"
        ])
    
    # Feelings
    elif any(question in user_input for question in feeling_questions):
        return random.choice([
            "I'm just a program, but thanks for asking! How can I help you?",
            "I'm here and ready to assist. How can I make your day easier?",
            "I'm functioning optimally! How about you?"
        ])
    
    # Help/Support
    elif any(keyword in user_input for keyword in help_keywords):
        return "I'm here to help! You can ask me about various topics, including weather, general knowledge, or just for a chat."

    # Weather
    elif any(keyword in user_input for keyword in weather_keywords):
        return "I'm unable to provide real-time weather updates, but I recommend checking a reliable weather website or app for the latest information."

    # Identity
    elif any(question in user_input for question in identity_questions):
        return "I'm a simple chatbot created to assist you with basic questions and provide company. Let's talk!"
    
    elif any(question in user_input for question in special_easter):
        return "I am created by Shivam Badhopulu for his internship TASK 1 given by CodeSoft in AI Domain.I am a simple chatbot created to assist you with basic questions and provide company. Let's talk!"
    # Generic 
    else:
        return random.choice([
            "I'm not sure I understand. Could you rephrase that?", 
            "Hmm, that doesn't sound familiar. Maybe try asking differently?", 
            "Can you clarify your question? I'll do my best to help!"
        ])

def start_chatbot():
    print("Chatbot: Hello! I'm here to assist you. Type 'bye' or 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in goodbyes:
            print("Chatbot:", chatbot_response(user_input))
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

start_chatbot()