height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2

bmi_round = (round(bmi, 2))
print(f"Your bmi is {bmi_round}")

if bmi < 18.5:
    print("You are underweight")

elif bmi < 25:
    print("You have a normal weight")

elif bmi < 30:
    print("You are overweight")

elif bmi <35:
    print("You are obese") 

else:
    print("You are clinically obese") 

