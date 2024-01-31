print("*")
print("Welcome To My Quiz Game")

question_bank = [
    {"text": "What is the capital city of Australia?", "answer": "C"},
    {"text": "In which year did the United States declare its independence?", "answer": "A"},
    {"text": "Who wrote the play 'Romeo and Juliet'?", "answer": "A"},
    {"text": "Which planet is known as the 'Red Planet'?", "answer": "B"},
    {"text": "What is the largest mammal in the world?", "answer": "B"},
    {"text": "What is the currency of Japan?", "answer": "A"},
    {"text": "Who is known as the 'Father of Modern Physics'?", "answer": "B"},
    {"text": "What is the largest ocean on Earth?", "answer": "D"},
    {"text": "In which year did the Berlin Wall fall, leading to the reunification of Germany?", "answer": "B"},
    {"text": "Which country is known as the 'Land of the Rising Sun'?", "answer": "B"}
]

options = [["A.Sydney","B.Melbourne","C.Canberra","D.Brisbane"],
           ["A.1776","B.1789","C.1801","D.1765"],
           ["A.William Shakespeare","B.Jane Austen","C.Charles Dickens","D.Mark Twain"],
           ["A.Venus","B.Mars","C.Jupiter","D.Saturn"],
           ["A.Elephant","B.Blue Whale","C.Giraffe","D.Polar Bear"],
           ["A.Yen","B.Yuan","C.Won","D.Ringgit"],
           ["A.Isaac Newton","B.Albert Einstein","C.Galileo Galilei","D.Niels Bohr"],
           ["A.Indian Ocean","B.Atlantic Ocean","C.Southern Ocean","D.Pacific Ocean"],
           ["A.1985","B.1989","C.1991","D.1979"],
           ["A.China","B.Japan","C.South Korea","D.Vietnam"]
]

score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter Your Answer (A/B/C/D):").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")

print(f"You have given {score} correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")