from src.Python100DaysChallenge.Day_17_OOP_Specific.QuizProgram.question_model import Question
from src.Python100DaysChallenge.Day_17_OOP_Specific.QuizProgram.data import  question_data
from src.Python100DaysChallenge.Day_17_OOP_Specific.QuizProgram.quiz_brain import QuizBrain

question_bank = []
#question_object = Question()
# for question in question_data:
#     print(question["text"],question["answer"])
for question in question_data:
    question_text= question["question"]
    question_answer = question["correct_answer"]
    question_object = Question(question_text,question_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the score")
print(f"your final score was : {quiz.score}/{len(question_bank)}")

