def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

monthly_income = get_float_input("Enter your monthly income: ")
rent =  get_float_input("Enter your monthly rent: ")
food = get_float_input("Enter your monthly food expenses: ")
entertainment = get_float_input("Enter your monthly entertainment expenses: ")
total_expenses = rent + food + entertainment
remaining_budget = monthly_income - total_expenses

print("======== buget summary =========")
print(f"Your monthly income is: ${monthly_income:.2f}")
print(f"Your total monthly expenses are: ${total_expenses:.2f}")
print(f"Your remaining budget is: ${remaining_budget:.2f}")
if remaining_budget <= 0:
    print("You're overspending! save some money!")
elif remaining_budget < 100:
    print("You're budget is tight. try to save more!")
elif remaining_budget >= 100:
    print("Great job! time to party!")