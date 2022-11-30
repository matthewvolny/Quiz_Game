from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    newQuestion = Question(question['text'], question['answer'])
    question_bank.append(newQuestion)

game_running = True

while game_running:

    quiz_brain = QuizBrain(question_bank)
    question_number = quiz_brain.question_number
    current_question = quiz_brain.get_question()
    user_answer = input(f"Q.{question_number}: {current_question.text} (True/False)?: ")
    
    if user_answer == current_question.answer:
        print("Correct! How about another question?")
        quiz_brain.increment_question()
    

    game_running = False
    

