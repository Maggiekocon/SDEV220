# This App asks users for a username and password, then it checks the credentials against authorized users.
# if the credentials are authentic then the app greats the user based on their role. 
# This app practices Confinentiality from the CIA triad. It ensures that users gain appropriate access based on their role. 

import sys
# predefined users: could be objects from a user class
user1 = {'username': 'Anna', 'password': 'Passw0rd', 'role': 'student'}
user2 = {'username': 'Maggie', 'password': 'Passw0rd1234', 'role': 'instructor'}

# User list for checking credentials
users = [user1, user2]


tryagain= 'yes'
while tryagain.lower() == "yes":
    username= input("What is your username? ")
    password= input("What is your password? ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            if user['role'] == 'student':
                print('Welcome student')
                sys.exit()
            else: 
                print('Welcome instructor')
                sys.exit()

    tryagain= input("These credentials do not exist. Would you like to try again? (yes/no) ")





## From Class
# Generates a list of prime numbers in a range
def primelist(lower,upper):
    primes = []
    for number in range(lower, upper+1):
        factors= []
        for i in range(1,number+1):
            print(i)
            if number%i == 0:
                factors.append(number)
        if len(factors)== 2:
            primes.append(number) 
    print(primes)  

# lower, upper = map(int, input("Enter range for your list of primes (e.g. 10,50): ").replace(',', ' ').split())      
# primelist(lower,upper)