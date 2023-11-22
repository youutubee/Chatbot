#Inilialise variables
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
    "9. The death"
    " anniversary of which of the following leaders is observed as Martyrs' Day?",
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
