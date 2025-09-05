guess_me = 5
for number in range(10):
    if number < guess_me:
        print("Too low")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("Oops!")
    