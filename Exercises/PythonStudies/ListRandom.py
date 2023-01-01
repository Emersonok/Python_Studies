import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_people = len(names)
random_name = random.randint(0, num_of_people - 1)
person_to_pay = names[random_name]

print(f"{person_to_pay} will pay the bill")

# OR - 
# person_to_pay = random.choice(names)





