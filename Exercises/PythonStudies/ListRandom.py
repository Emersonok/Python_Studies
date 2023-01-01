
import random
random_name = input("Write your names separated by a comma ")
names = random_name.split(',') #names of the people
num_of_people = len(names)
rand_name = random.randint(0, num_of_people - 1) #random name to be selected
payer = rand_name[names]
print(f"{payer} will pay the bill")
# person_to_pay = random.choice(names)







