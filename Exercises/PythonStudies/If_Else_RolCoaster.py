print("Welcome to the Roller Coaster! Follow the instructions")
name = input("What is your name? ")
height = int(input("What is your height in cm? "))
bill = 0 # use 0 to attribute a first value that can change

if height > 120:
    print(f"Hi {name}! Your height is {height}, welcome to the Roller Coaster")
    age = int(input("How old are you? "))
    if age >= 45 and age <= 55:
        bill = 0
        print("Free ticket for you") 

    if age > 55:
        bill = 12
        print(f"Adult ticket is $12. Thanks {name}!")
    
    elif age < 12:
        bill = 5
        print(f"Kids ticket is $5. Thanks {name}!")
    else:
        bill = 7
        print(f"Youth is $7. Thanks {name}!")

    photo = input("Do you want a photo? Y or N ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")


else:
    print(f"Sorry {name}! Your height is {height}, can't get in")
