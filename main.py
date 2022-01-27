from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i["text"]
    answer = i["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()
else:
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
