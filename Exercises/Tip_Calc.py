print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip_percentage = input("What tip percentage would you like to give? 10, 12, or 15? " )
split = input("How many people to split the bill? ")

bill_int = float(bill)
tip_percentage_int = int(tip_percentage)
split_int = int(split)

tip_value = (tip_percentage_int / 100) * bill_int
bill_value = tip_value + bill_int
bill_per_person = bill_value / split_int

Amount = (round(bill_per_person, 2))
Amount = "{:.2f}".format(bill_per_person) # to add a second zero while rounding the decimals
print(f"Each person pays ${Amount}")