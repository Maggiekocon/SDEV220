small = False
green = False

Condition  = [small, green] 

choices = ['Cherry', 'Pea', 'Watermelon', 'Pumpkin']

for choice in choices:
    if choice == 'Cherry':
        results = [True, False]
        if results == Condition:
            print(choice)
    elif choice == "Pea":
        results = [True, True]
        if results == Condition:
            print(choice)
    elif choice == 'Watermelon':
        results = [False, True]
        if results == Condition:
            print(choice)
    elif choice == 'Pumpkin':
        results = [False, False]
        if results == Condition:
            print(choice)
