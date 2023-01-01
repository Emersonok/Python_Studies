#printing the max/min value in list

grades = [30, 7, 90, 10, 10, 2]
max = grades[0]
min = grades [0]

for x in grades:
    if x > max:
        max = x
    if x < min:
        min = x

print(f"The highest grade is {max} and the lowest grade is {min}")


     
    
