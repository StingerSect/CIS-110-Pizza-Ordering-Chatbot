# Rashim Rabess CIS 110 Week 6

print("Hello, my name is Ethan your vitural assistant. I will help you order a pizza!")
print("To get started, I need to know how to address you. Please press enter after each response")
userName = input("\nEnter your name: ")
while len(userName) == 0:
    userName = input("\nName cannot be blank. Please enter your name: ")
if userName.lower() == "rashim r":
    print(f"\nMy Creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nWelcome to Pizza Paradise {userName}.")


keepGoing = "yes"
while keepGoing.lower() == "yes":
    
    size = input("\nWhat size do you want? Enter small, medium, or large: ")
    while size.lower() not in ["small", "medium", "large"]:
        size = input("\nInvaild Entry. Please enter small, medium, or large: ")
    flavor = input("\nEnter the flavor of pizza: ")
    while len(flavor) == 0:
        flavor = input("\nFlavor cannot be blank. Please enter a flavor: ")
    crustType = input("\nWhat type of crust do you want: ")
    while len(crustType) == 0:
        crustType = input("\nCrust type cannot be blank. Please enter a crust type: ")
    quaninty = input("\nHow many of these do you want to order? Enter a numeric value: ")
    while not quaninty.isdigit():
        quaninty = input("\nValue not recognized. Please enter a numeric value: ")
    quaninty = int(quaninty)
    method = input("\nIs this carry out or delivery: ")
    while method.lower() not in ["carry out", "delivery"]:
        method = input("\nInvaild Entry. Please enter carry out or delivery: ")

    salesTax = 1.1
    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99

    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0

    total = (pizzaCost * quaninty) * salesTax + deliveryFee

    print("-" * 10)
    print(f"Thank you, {userName}, for your order.")
    print(f"Your {quaninty} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")

    if total >= 50:
        print("\nCongratulations! You've been awarded a $10 off coupon  for your next order.")
    else:
        print("\nOrders over $50 will receive a free $10 off coupon!")

    print("-" * 10)
    print("Order has been received. ETA 3 Mins!")
    for min in range(3, 0, -1):
        print(min, "Minutes Remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = "\r" )
            import time
            time.sleep (1)
    print("Order is ready!")
    keepGoing = input("\nDo you want to place another order? Enter yes or no:  ")
    while keepGoing.lower() not in ["yes", "no"]:
        keepGoing = input("Invaild: Enter yes or no:  ")

