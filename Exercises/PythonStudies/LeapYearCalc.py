print("Welcome to Leap Year Calculator")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          print(f"Year {year} is a leap")
        else:
            print("Not Leap Year")

    else:
        print("Leap Year")
    
else: 
    print(f"Year {year} is not a Leap Year")
        