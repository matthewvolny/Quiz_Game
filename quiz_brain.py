class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 1
        self.question_bank = question_bank

    def increment_question(self):
        self.question_number += 1

    def get_question(self):
        return self.question_bank[self.question_number]    