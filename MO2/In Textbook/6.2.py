import random 

guess_me = random.randint(1,10)

number = 1

while number != guess_me:
    if number < guess_me:
        print("Too low! ")
    else:
        print("oops! ")

    number += 1 

print("found it!")
exit()