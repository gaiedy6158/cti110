# Calculating and displaying travel expenses
# 9/26/2023
# CTI-110 P1HW2 - Travel Expense
# Yousab Gaied
print("This program calculates and displays travel expenses")
# Get user input for budget, destination, gas, accommodation, and food expenses
budget = float(input("Enter Budget: $"))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas?: $"))
accommodation_expense = float(input("Approximately, how much will you need for accomodation/hotel?: $"))
food_expense = float(input("Last, how much do you need for food?: $"))

# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate the remaining budget
remaining_budget = budget - total_expenses

# Display the results with explanations
print("------------Travel Expense------------")
print("Initial Budget: $", budget)

print("Fuel: $", gas_expense)
print("Accommodation: $", accommodation_expense)
print("Food: $", food_expense)

print("Remaining Balance: $", remaining_budget)

# End of the program
