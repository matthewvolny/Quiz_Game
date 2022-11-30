from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    newQuestion = Question(question['text'], question['answer'])
    question_bank.append(newQuestion)

def game():
    
    continue_game = True
    quiz_brain = QuizBrain(question_bank)

    while continue_game:

        question_number = quiz_brain.question_number
        current_question = quiz_brain.get_question()
        user_answer = input(f"Q.{question_number}: {current_question.text} (True/False)?: ")
        
        if user_answer == current_question.answer:
            print("Great job! Here is another one.")
            quiz_brain.increment_question()
        else:
            print("Sorry that is incorrect.")
            try_again = input("Would you like to play again (True/False)?: ")
            if try_again == True:
                game()
            else:    
                print("Goodbye.")
                continue_game = False

game()
    

