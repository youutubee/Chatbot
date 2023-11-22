import json
from timee import time_ge#module for Timw
import subprocess #module for calculator
from Kbc import play_kbc
from assignment import open_assignment

def cal():
    subprocess.Popen(["open", "-a", "Calculator"])
def load_from_json():
    try:
        with open("knowledge_base.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

# Function to save the dictionary to a JSON file
def save_to_json(data):
    with open("knowledge_base.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

# Function to get a response from the dictionary
def get_response(question):
    qa_dict = load_from_json()
    return qa_dict.get(question.lower(), "I don't know the answer. Can you teach me? Type 'teach' to proceed.")

# Function to teach the chatbot
def teach():
    new_question = input("Please enter the new question: ")
    new_answer = input("Please enter the answer: ")

    qa_dict = load_from_json()
    qa_dict[new_question.lower()] = new_answer
    save_to_json(qa_dict)

    return "Thank you for teaching me! Now I know the answer."

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "teach":
        response = teach()
    elif user_input.lower() == "what is the time":
        print("The time right now is")
        time_ge()
    elif user_input.lower() == "open calculator":
        print("Sure Opening Calculator")
        cal()
    elif user_input.lower() == "assignment":
        open_assignment()
    elif user_input.lower() == "i would like to play a game":
        print("Bot: Sure! Here are the available games:")
        print("1. Kaun Banega Crorepati (KBC)")
        game_choice = input("You can type the name of the game you want to play: ").strip().lower()
        if game_choice == "kbc" or game_choice == "1":
            print("Bot: Welcome to Kaun Banega Crorepati (KBC)!")
            play_kbc()
            money = 5000  # Reset money for the next game
        else:
            print("Bot: Sorry, I don't have that game.")
    else:
        response = get_response(user_input)
        print("Bot:", response)
