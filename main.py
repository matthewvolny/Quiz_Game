from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    newQuestion = Question(question['text'], question['answer'])
    question_bank.append(newQuestion)

print(question_bank[0].text)
print(question_data[0]['text'])