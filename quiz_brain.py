class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.player_score = 0

    def increment_question(self):
        self.question_number += 1
    
    def get_current_question(self):
        return self.question_bank[self.question_number]
    
    def ask_question(self):
        current_question = self.get_current_question()
        return input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
    
    def check_user_answer(self, user_answer):
        current_question = self.get_current_question()
        if user_answer == current_question.answer:
            self.player_score += 1
            return True
        else:
            return False

    def display_correct_answer(self):
        current_question = self.get_current_question()
        return print(f"The correct answer was: {current_question.answer}")

    def display_score(self):
        return print(f"Your current score is: {self.player_score}/{self.question_number + 1}.")
        
    def still_has_questions(self):
        next_question = self.question_number + 1
        if next_question < len(self.question_bank):
            return True
        else:
            return False   