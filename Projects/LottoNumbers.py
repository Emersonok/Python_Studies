import random
def numbers():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    random_number = random.choice(list_of_numbers)
    return random_number

lotto_numbers = []


for x in range(15):
    lotto_numbers.append(numbers())
    if x in lotto_numbers:
        continue
print(lotto_numbers)