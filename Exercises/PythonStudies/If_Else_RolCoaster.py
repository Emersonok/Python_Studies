print("Welcome to the Roller Coaster! Follow the instructions")
name = input("What is your name? ")
height = int(input("What is your height in cm? "))

if height > 120:
    print(f"Hi {name}! Your height is {height}, welcome to the Roller Coaster")
    age = int(input("How old are you? "))
    if age >= 18 and age <= 60:
        print(f"Your ticket is $12. Thanks {name}!")
    elif age > 60:
        print(f"Hi {name}, you are too old for this, please go home and rest!!")
    elif age < 12:
        print(f"Your ticket is $5. Thanks {name}!")
    else:
        print(f"Your ticket is $7. Thanks {name}!")


else:
    print(f"Sorry {name}! Your height is {height}, can't get in")
