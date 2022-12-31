print("Welcome to Python Pizza Deliveries! ")
size = input("What size pizza do you? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y, N ")
extra_cheese = input("Do you want extra cheese? Y, N ")

bill = 0

if size == "S":
    bill = 15
    print(f"Small pizza costs ${bill}")
    if add_pepperoni == "Y":
        bill += 2
        print(f"With pepperoni, bill is ${bill}")
    if extra_cheese == "Y":
        bill += 1
        print(f"With extra cheese, bill is ${bill}")


if size == "M":
    bill = 20
    print(f"Mesium pizza costs ${bill}")
    if add_pepperoni == "Y":
        bill += 3
        print(f"With pepperoni, bill is ${bill}")
    if extra_cheese == "Y":
        bill += 1
        print(f"With extra cheese, bill is ${bill}")


if size == "L":
    bill = 25
    print(f"Large pizza costs ${bill}")
    if add_pepperoni == "Y":
        bill += 3
        print(f"With pepperoni, bill is ${bill}")
    if extra_cheese == "Y":
        bill += 1
        print(f"With extra cheese, bill is ${bill}")