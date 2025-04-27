# Rashim Rabess CIS 110 Week 3
print("Hello, my name is Ethan your vitural assistant. I will help you order a pizza!")
print("To get started, I need to know how to address you. Please press enter after each response")
userName = input("\nEnter your name: ")
print(f"\nWelcome to Pizza Paradise {userName}.")
size = input("\nWhat size do you want? Enter small, medium, or large: ")
flavor = input("\nEnter the flavor of pizza: ")
crustType = input("\nWhat type of crust do you want: ")
quaninty = input("\nHow many of these do you want to order? Enter a numeric value: ")
quaninty = int(quaninty)
method = input("\nIs this carry out or delivery: ")

salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quaninty) * salesTax

print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {quaninty} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)