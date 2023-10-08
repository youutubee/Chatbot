import datetime #module for Timw
import subprocess #module for calculator
#Calculator Function
def cal():
    subprocess.Popen(["open", "-a", "Calculator"])


# Define a question/answer dictionary
qa_dict = {
    "hello":"Hello",
    "what is your name": "My name is Dialogix",
    "how are you today": "I don't have feelings, but I'm here to help!",
    "who created you": "I was created by Algo_Avengers .",
    "what is the meaning of life": "The meaning of life is a philosophical question that has no single answer.",
    "goodbye": "Goodbye! Feel free to ask more questions anytime.",
}

# Function to get a response from the dictionary
def get_response(question):
    return qa_dict.get(question, "I don't understand that question.")

# Initialize variables for kbc game
money = 5000
count = 0

# Questions, options, and answers for the KBC game
questions = [
    "1. The International Literacy Day is observed on",
    "2. The language of Lakshadweep, a Union Territory of India, is",
    "3. In which group of places is the Kumbha Mela held every twelve years?",
    "4. Bahubali festival is related to",
    "5. Which day is observed as World Standards Day?",
    "6. Which of the following was the theme of the World Red Cross and Red Crescent Day?",
    "7. September 27 is celebrated every year as",
    "8. Who is the author of 'Manas Ka-Hans'?",
    "9. The death anniversary of which of the following leaders is observed as Martyrs' Day?",
    "10. Who is the author of the epic 'Meghdoot'?"
]

options = [
    "A. Sep 8\nB. Nov 28\nC. May 2\nD. Sep 22",
    "A. Tamil\nB. Hindi\nC. Malayalam\nD. Telugu",
    "A. Ujjain, Purl, Prayag, Haridwar\nB. Prayag, Haridwar, Ujjain, Nasik\nC. Rameshwaram, Purl, Badrinath, Dwarika\nD. Chittakoot, Ujjain, Prayag, Haridwar",
    "A. Islam\nB. Hinduism\nC. Buddhism\nD. Jainism",
    "A. June 26\nB. Oct 14\nC. Nov 15\nD. Dec 2",
    "A. 'Dignity for all - focus on women'\nB. 'Dignity for all - focus on Children'\nC. 'Focus on health for all'\nD. 'Nourishment for all-focus on children'",
    "A. Teachers' Day\nB. National Integration Day\nC. World Tourism Day\nD. International Literacy Day",
    "A. Khushwant Singh\nB. Prem Chand\nC. Jayashankar Prasad\nD. Amrit Lal Nagar",
    "A. Smt. Indira Gandhi\nB. Pt. Jawaharlal Nehru\nC. Mahatma Gandhi\nD. Lal Bahadur Shastri",
    "A. Vishakadatta\nB. Valmiki\nC. Banabhatta\nD. Kalidas"
]

answers = ["A", "C", "B", "D", "B", "B", "C", "D", "C", "D"]

# Function to play the KBC game
def play_kbc():
    global money, count
    for i in range(10):
        print("\n" + questions[i])
        print("\n" + options[i])
        ans = input("\nYour answer (A, B, C, or D): ").upper()
        if ans == answers[i]:
            money *= 2
            count += 1
            print("\nCorrect! You won", money, "Rupees")
        else:
            print(f"\nBetter luck next time \nYou answered {count} question(s) correctly and won {money} Rupees")
            break

    # Check if all questions were answered correctly
    if count == 10:
        print("Congratulations! You answered all questions correctly and won a whopping", money, "Rupees")
def time_ge():

    # Get the current local time
    current_time = datetime.datetime.now()

    # Format the local time as a string
    formatted_time = current_time.strftime("%H:%M:%S")

    # Print the formatted local time
    print(formatted_time)


# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "what is the time":
        print("The time rignt now is")
        time_ge()
    elif user_input.lower() == "open calculator":
        print("Sure Opening Calculator")
        cal()
    elif user_input.lower() == "i would like to play a game":
        print("Bot: Sure! Here are the available games:")
        print("1. Kaun Banega Crorepati (KBC)")
        game_choice = input("You can type the name of the game you want to play: ").strip().lower()
        if game_choice == "kbc" or game_choice=="1":
            print("Bot: Welcome to Kaun Banega Crorepati (KBC)!")
            play_kbc()
            money = 5000  # Reset money for the next game
        else:
            print("Bot: Sorry, I don't have that game.")
    else:
        response = get_response(user_input)
        print("Bot:", response)
