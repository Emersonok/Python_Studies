import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#nr_letters= int(input("How many letters would you like in your password?\n")) 
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))

#password = ""
#for letter in range(1, nr_letters + 1): 
 #   password += random.choice(letters)

#for symbol in range(1, nr_symbols + 1):
  #  password += random.choice(symbols)

#for number in range(1, nr_numbers + 1):
 #   password += random.choice(numbers)

#print(password)

#password = []

#for letter in range(1, nr_letters + 1):
 #   password += random.choice(letters)

#for symbol in range(1, nr_symbols + 1):
 #   password.append(random.choice(symbols))

#for number in range(1, nr_numbers + 1):
 #   password += random.choice(numbers)

#random.shuffle(password)

#final_password = ""
#for word in password:
 #   final_password += word

#print(final_password)

select = input("Write 'Yes' to generate your password automatically,\nWrite 'No' to enter your password ")
select = select.upper()
password = [] #password a list so it can be shuffled
if select == "NO":
    enter = input("Enter your password ")
    print(f"Your password is: {enter}")

elif select == "YES":
    for letter in range(1, 5):
      password += random.choice(letters)

    for symbol in range(1, 4):
        password += random.choice(symbols)

    for number in range(1, 4):
        password += random.choice(numbers)

    random.shuffle(password)
    
    final_password = "" #change password back to string after shuffling
    for word in password:
        final_password += word

    print(f"Your password is {final_password}")
    




      





