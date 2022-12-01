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

        user_answer = quiz_brain.ask_question()
        
        if quiz_brain.check_user_answer(user_answer) == True:
            print("You got it right!")
            quiz_brain.display_correct_answer()
            quiz_brain.display_score()
            print("\n")

            if quiz_brain.still_has_questions() == True:
                quiz_brain.increment_question()
            else:
                print("You got all questions correct!")
                print("Goodbye.")
                continue_game = False
        else:
            print("Sorry that is incorrect.")
            try_again = input("Would you like to play again (True/False)?: ")
            if try_again == True:
                game()
            else:    
                print("Goodbye.")
                continue_game = False

game()
    

