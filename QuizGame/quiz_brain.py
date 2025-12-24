class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        currQuestion = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {currQuestion.text}\nTrue or False: ").lower()
        self.check_answer(user_answer, currQuestion.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score +=1 
            print("That is correct!")
        else:
            print(f"That is incorrect.\nThe correct answer is: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def get_final_score(self):
        print("You have completed the quiz!!!!")
        print(f"Your final score is: {self.score}/{self.question_number}")
