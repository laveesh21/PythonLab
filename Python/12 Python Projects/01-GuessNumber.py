import random

def guess(x):
    randNum = random.randint(1,x)
    guess = 0
    while guess != randNum:
        guess = int(input("Guess a number: "))
        if guess < randNum:
            print("Number is Lower.")
        elif guess > randNum:
            print("number is Greater")
        else:
            print("You Got the number right!")
            break


x = input("Enter random number max range: ")
guess(int(x))
