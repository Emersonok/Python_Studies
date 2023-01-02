#fruits = ["Apple", "Peach", "Pie"]
#for x in fruits:
 #   print(x + x)

#num = [2, 4, 6]
#for y in num:
 #   print(y + y)

#sum_of_heights = sum(student_heights)
#num_of_students = len(student_heights)
#average = round(sum_of_heights / num_of_students)
#print(f"The average height is {average}")

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) # do this cos it's a list of numbers, changing them all to int. Use n as a range too

heights = 0
for add_heights in student_heights:
    heights += add_heights # heights = heights + add_heights
print(heights)

length_of_heights = 0
for count_heights in student_heights:
    length_of_heights = length_of_heights + 1 # length_of_heights += 1

print(length_of_heights)

average_height = round(heights / length_of_heights)
print(f"The average student height is {average_height}")

