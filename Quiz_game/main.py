from data import question_data
from question_module import Question
from QuizBrain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")




# Below code is without using classes and objects

# game_on=True
# score=0
# x=0
# while game_on:
#     for q in question_data:
#         ans=input(f"Q.{x+1}: {question_data[x]['text']} (True/False):  ")
#         a=question_data[x]["answer"]
#         if ans == a:
#             print("You got it right!")
#             score+=1
#             x+=1
#             print(f"The correct answer was: {a}")
#             print(f"Your score is : {score}")
#         else:
#             print("That's wrong!")
#
#             print(f"The correct answer was: {a}")
#             print(f"Your score is : {score}")
#             game_on=False
#             break
