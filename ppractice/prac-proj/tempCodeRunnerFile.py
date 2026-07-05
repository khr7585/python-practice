import random
print("game started")
while True:
    number=random.randint(1,10)
    attempts=0
    while True:
        guess=int(input("guess the number from 1 to 10:"))
        attempts+=1
        if guess==number:
            print("congratulations")
            print("Number of attempts=",attempts)
            break
        elif guess<number:
            print("Too Low")
        else:
            print("Too High")
    again=input("do you want to guess again(yes/no):").lower()
    if again=='yes':
        continue
    elif again=='no':
        print("thanks for playing!")
        break
    else:
        print("invalid input & program stopped...")
        break