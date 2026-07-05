# 1.CALCULATOR
# print("start")
# while True:
#      num1=float(input("enter your first number:"))
#      num2=float(input("enter your second number:"))
#      op=input("choose your operation(+,-,*,/):")
#      if op=="+":
#          print("result",num1+num2)
#      elif op=="-":
#          print("result",num1-num2)
#      elif op=="*":
#          print("result",num1*num2)
#      elif op=="/":
#          if num2!=0:
#              print("result",num1/num2)
#          else:
#              print("0 is not divided")
#      else:
#          print("invalid operator")
#      user=input("Do you want to calculate more(yes/no)?:").lower()
#      if user=="no":
#          print("thank you for using this calculator!")
#          break

#2.NUMBER GUESSING GAME
# import random
# print("game started")
# while True:
#     number=random.randint(1,10)
#     attempts=0
#     while True:
#         guess=int(input("guess the number from 1 to 10:"))
#         attempts+=1
#         if guess==number:
#             print("congratulations")
#             print("Number of attempts=",attempts)
#             break
#         elif guess<number:
#             print("Too Low")
#         else:
#             print("Too High")
#     again=input("do you want to guess again(yes/no):").lower()
#     if again=='yes':
#         continue
#     elif again=='no':
#         print("thanks for playing!")
#         break
#     else:
#         print("invalid input & program stopped...")
#         break

#3.PASSWORD GENERATOR
# import random
# import string
# print("=====PASSWORD GENERATOR=====")
# while True:
#     length=int(input("enter a password length:"))
#     characters=(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
#     password=""
#     for i in range(length):
#         password+=random.choice(characters)
#     print("generate password:",password)
#     break

#4.TO-DO-LIST
# print("START")
# tasks=[]
# print("MENU")
# while True:
#     print("1. ADD TASK")
#     print("2. VIEW TASKS")
#     print("3. REMOVE TASK")
#     print("4. EXIT")
#     choice=int(input("choose an option(1-4):"))
#     if choice==1:
#         task=input("enter a task:")
#         tasks.append(task)
#         print("task added successfully!")
#     elif choice==2:
#         print(tasks)
#     elif choice==3:
#         task=input("enter a task to remove:")
#         if task in tasks:
#             tasks.remove(task)
#             print("task removed successfully!")
#         else:
#             print("task not found!")
#     elif choice==4:
#         break

#4.ROCK PAPER SCISSORS
# import random
# print("=====G@ME ST@RTED=====")
# choices=['rock','paper','scissors']
# while True:
#     user=input("enter rock , paper , scissors:").lower()
#     if user not in choices:
#         print("invalid choice! please follow the input...")
#         continue
#     system=random.choice(choices)
#     print("your choice:",user)
#     print("computer choice:",system)
#     if user==system:
#         print("its a tie!")
#     elif (user=="rock" and system=="paper") or (user=="paper" and system=="scissors") or (user=="scissors" and system=="rock"):
#         print("computer wins!")
#     else:
#         print("congratulations! you win!")
#     again=input("do you want to play again(yes/no):").lower()
#     if again=="yes":
#         continue
#     elif again=="no":
#         print("Thnaks for playing!")
#         break
#     else:
#         print("invalid input.program stopped...")
#         break

#5.QUIZ GAME
# score=0
# questions=[
#     {
#         "question": "1. Which planet in our sloar system has the shortest day?",
#         "options": ["A. Mars", "B. Jupiter", "C. Saturn", "D. Mercury"],
#         "answer": "B" 
#     },
#     {
#         "question": "2. Which country has the largest number of time zones?",
#         "options": ["A. russia", "B. united states", "C. france", "D. australia"],
#         "answer": "C"
#     },
#     {
#         "question": "3. What is the chemical symbol for tungsten?",
#         "options": ["A. tg", "B. tu", "C. w", "D. tn"],
#         "answer": "C"
#     },
#     {
#         "question": "4. Who developed the theory of general realtively?",
#         "options": ["A. issac newton", "B. galileo galilei", "C. albert einstein", "D. nikola tesla"],
#         "answer": "C"
#     },
#     {
#         "question": "5. Which is the deepest ocean trench on earth?",
#         "options": ["A. puerto rico trench", "B. java trench", "C. mariana trench", "D. peru-chile trench"],
#         "answer": "B"
#     }
# ]
# print("=====WELCOME TO QUIZ GAME=====")
# for q in questions:
#     print("\n"+q["question"])
#     for option in q["options"]:
#         print(option)
#     user_answer=input("enter your answer(A/B/C/D):").upper()
#     if user_answer==q["answer"]:
#         print("correct!")
#         score+=1
#     else:
#         print("wrong!")
#         print("correct answer:",q["answer"])
# print("=====quiz finished!=====")
# print(f"your score:{score}/{len(questions)}")
# percentage=(score/len(questions))*100
# print(f"percentage:{percentage:.2f}%")
# if percentage==100:
#     print("EXCELLENT!")
# elif percentage>=80:
#     print("VERY GOOD!")
# elif percentage>=60:
#     print("GOOD JOB!")
# elif percentage>=40:
#     print("KEEP PRACTICING!")
# else:
#     print("BETTER LUCK NEXT TIME")