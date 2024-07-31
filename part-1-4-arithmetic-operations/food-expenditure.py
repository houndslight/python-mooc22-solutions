number1 = int(input("How many times a week do you eat at the student cafeteria? "))
number2 = float(input("The price of a typical student lunch? "))
number3 = float(input("How much money do you spend on groceries in a week? "))


cafeteria_cost = number1 * number2

total_weekly_expenditure = cafeteria_cost + number3

daily_expenditure = total_weekly_expenditure / 7

print("Average food expenditure:")
print(f"Daily : {daily_expenditure:.2f}")
print(f"Weekly: {total_weekly_expenditure:.2f}")