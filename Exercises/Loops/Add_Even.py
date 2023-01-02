even_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_number += number # even_number = even_number + number
print(even_number)

total2 = 0 
for number in range(2, 101, 2):
    total2 += number
print(total2)