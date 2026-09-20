item1 = float(input("Enter the cost of the first item: "))
item2 = float(input("Enter the cost of the second item: "))

total_cost = item1 + item2

print(f"Total cost: ${total_cost:.2f}")

payment = float(input("Enter your payment: $"))

if payment < total_cost:
    amount_owed = total_cost - payment
    print(f"You still owe: ${amount_owed:.2f}")
else:
    change = payment - total_cost
    print(f"Thank you for your payment!")
    print(f"Your change is: ${change:.2f}")