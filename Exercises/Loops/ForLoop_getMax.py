student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

#easy way - 
#print(max(student_scores))# - 0(1) running time

#now we want 0(N) running time complexity
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

total = 0
for number in range(0, 101):
    total += number # total = total + number
print(total)