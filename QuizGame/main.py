from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

brain.get_final_score()