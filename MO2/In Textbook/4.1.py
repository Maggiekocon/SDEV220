import random 

secret = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    if guess < secret:
        print("Too low! ")
    else:
        print("Too high! ")

    guess = int(input("Guess Again: 2")) 

print("Just right!")
exit()