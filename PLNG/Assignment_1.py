# HILVANO, STEVEN REIGN S.
# BSCS 2-Y1-1
# ACTIVITY 1
#For the sample scores 78, 87, and 77, the result is:

#Average: 80.67
#Grade: B
#Do you want to continue? (YES/NO): NO
#Program terminated. Thank you!


while True:
    print("Activity 1 - Student Grade Calculator")

    java_score = float(input("Java Programming Score: "))
    c_score = float(input("C Programming Score: "))
    database_score = float(input("Database Handling Score: "))

    # Calculate the average
    average = (java_score + c_score + database_score) / 3

    # Determine the grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 75:
        grade = "C"
    else:
        grade = "F"

    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    choice = input("Do you want to continue? (YES/NO): ").upper()

    if choice == "NO":
        print("Program terminated. Thank you!")
        break