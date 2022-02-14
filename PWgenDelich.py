import random

#var declaration
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
special = "!#$%^&*+"
length = 10
amount = 5
combine = ""
lower = True
upper = True
number = True
spec = True

#method for checking user input
def ask_user():
    global lower, upper, number, spec, length, amount, check
    check = input("What length would you like your password to be? ")
    try:
        if  check.strip().isdigit():
            length = check
            length = int(length)
        else:
            print("invalid input. input must be number")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()
    check = input("How many passwords would you like to generate? ")
    try:
        if check.strip().isdigit():
            amount = check
            amount = int(amount)
        else:
            print("invalid input. input must be number")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()
    check = str(input("Do you want to include lowercase characters? (Y/N)")).lower().strip()
    try:
        if check[0] == "y":
            lower = True
        elif check[0] == "n":
            lower = False
        else: 
            print("invalid input")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()
    check = str(input("Do you want to include uppercase characters? (Y/N)")).lower().strip()
    try:
        if check[0] == "y":
            upper = True
        elif check[0] == "n":
            upper = False
        else: 
            print("invalid input")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()
    check = str(input("Do you want to include number characters? (Y/N)")).lower().strip()
    try:
        if check[0] == "y":
            number = True
        elif check[0] == "n":
            number = False
        else: 
            print("invalid input")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()
    check = str(input("Do you want to include special characters? (Y/N)")).lower().strip()
    try:
        if check[0] == "y":
            spec = True
        elif check[0] == "n":
            spec = False
        else: 
            print("invalid input")
            return ask_user()
    except:
        print("Please enter valid inputs")
        return ask_user()

#executing the function to get info
ask_user()

#cheking which combination is selected
if lower:
    combine += lowercase
if upper:
    combine += uppercase
if number:
    combine += nums
if spec:
    combine += special

for x in range(amount):
        temp = random.sample(combine, length)
        password = "".join(temp)
        print(password)