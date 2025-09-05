# Maggie Kocon
# StudentStatus
# This app tells the user their student status based on their GPA.

lname=input("Enter your last name: ")

while lname != 'ZZZ':
    fname=input("Enter your first name: ")
    GPA=float(input("Enter your GPA: "))
    if GPA >= 3.5:
        print(f"Congradulations {fname}! You made the Dean's list! ")
        lname='ZZZ'
    elif GPA >= 3.25:
        print(f"Congradulations {fname}! You made the Honor Roll! ")
        lname='ZZZ'

    lname=input("Enter your last name: ")

exit()