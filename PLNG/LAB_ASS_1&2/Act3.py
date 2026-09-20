number = int(input("Enter a multiple of 5 between 1 and 100: "))

if number >= 1 and number <= 100 and number % 5 == 0:
    print("The number is valid.")
else:
    print("The number is invalid.")
    