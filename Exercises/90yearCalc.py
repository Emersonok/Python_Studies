age = input("What is your current age? ")
Your_age = int(age)
Ninety_years_days = 365 * 90
Ninety_years_weeks = 52 * 90
Ninety_years_months = 12 * 90

Your_days = Your_age * 365
Your_weeks = Your_age * 52
Your_months = Your_age * 12

Days_left = Ninety_years_days - Your_days
Weeks_left = Ninety_years_weeks - Your_weeks
Months_left = Ninety_years_months - Your_months

print(f"You have {Days_left} days, {Weeks_left} weeks, and {Months_left} months left  ")