height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

square_height = new_height ** 2

bmi = new_weight / square_height

print(round(bmi))