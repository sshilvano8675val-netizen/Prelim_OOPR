# Program 1
# How to print “Hello World” on Python?

print("Hello World")

# Program 2
# How to print “Hello + Username” with the user’s name on Python?

usertext = input("What is your name? ")
print("Hello", usertext)

#Program 3
#How to add 2 numbers entered on Python?
num1 = input('Enter the first number:')
num2 = input('Enter the Second number')
sum = float(num1) + float(num2)

print('the sum of {0} and {1} is {2}'. format(num1, num2, sum))

# Program 4
# How to find the Average of 2 Entered Numbers on Python?

num1 = input('Enter the first number:')
num2 = input('Enter the Second number')
average = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#Program 5
#How to calculate the Entered Visa and Final Grade Average on Python?

visagrade = input('enter your visagrade: ')
finalgrade = input('Enter your final gradee')
average = (float(visagrade)*0.3)+(float(finalgrade)*0.7)
print("average :{0}".format(average))

#Program 6
#How to find the Average of 3 Written Grades entered on Python?

firstexam = input('your first exam : ')
secondexam = input('your second exam : ')
thirdexam = input('your third exam : ')
average =(float(firstexam)+float(secondexam)+float(thirdexam))/3
print("average :{0} ".format(average))

#Program 7
#How to show the Class Pass Status (PASSED — FAILED) of the Student whose Written Average Has Been Entered on Python?

average = input('enter average ')
if int(average)>=50:
 print("passed")
else:
 print("Failed")

# Program 8
# How to find out if the entered number is odd or even on Python?

num = int(input("Enter a Number: "))
if (num % 2) == 0:
    print("{0} is Even". format(num))
else:
  print("{0} is odd", (num))

#Program 8
#How to find out if the entered number is odd or even on Python?

num = float(input("Enter a number: "))
if num > 0:
  print("Positive number")
elif num == 0:
  print("Zero")
else:
  print("Negative number")

#program 10
#How to calculate body mass index on Python?

print("body mass index calculation program")
height = float(input("enter height (m):"))
weight = int(input("enter weight (kg):"))
index = weight/(height*height)
if index <=18:
 print("\n underweight BMİ:{}".format(index))
elif index > 18 and index <=25 :
 print("\n overweight BMİ:{}".format(index))
elif index > 25 and index <=30:
 print("\n obese BMİ:{}".format(index))
elif index > 30:
 print("\n severely obese BMİ:{}".format(index))

#Program 11
#How to show if the person whose age is entered can get a driver’s license on Python?

age = input('enter age : ')
if(int(age)<18):
 print("Your Age Is Not Eligible To Get A Driver's License")
else:
 print("Your Age Is Eligible To Get Your License")

#Program 12
#How to List Numbers 1–100 on the Screen on Python?

for i in range(1,101):
 print(i)

#Program 13
#How to List Even Numbers 1–100 on Python?

for i in range(1,101):
 if i%2==0:
  print(i)

#Program 14
#How to List Odd Numbers from 1–100 on Python?

for i in range(1,101):
 if i%2!=0:
  print(i)

#Program 15
#How to find numbers between 1 and 100 that are divided by 3 and 5 on Python?

for i in range(1,101):
  if i%3==0 or i%5==0:
   print(i)

#Program 16
#How to list Numbers from 1 to User-Entered Number on Python?

num = input('enter number : ')
for i in range(1,int(num)+1):
  print(i)
#Program 17
#How to find the Area and Perimeter of a Rectangle With Its Sides on Python?

short = input('Enter short side : ')
tall = input('Enter tall side : ')
area = int(short)*int(tall)
perimeter =2*(int(short)+int(tall))
print("area: {0}".format(alan))
print("perimeter: {0}".format(cevre))

#Program 18
#How to print the letters of the entered text one under the other on Python

word = 'mrhuseyin'
for char in word:
 print(char)

#Program 19
#How to show the sum of numbers between two numbers the user has entered on Python?

sumofnumbers=0;
num1 = input('first number: ')
num2 = input('second number: ')
for i in range(int(sayi1)+1,int(sayi2)):
 sumofnumbers+=i
 print("Sum of numbers between {0} and {1} : {2}".format(num1,num2,sumofnumbers))

#Program 20
#For example, let’s ask the user about their choice of cinema or theater. You have to pay 10 dollars towatch movies and 5 dollars for theater. We think that students get 50% discount. If the student is discounted; If he is not a student, let’s write a document that calculates the non-discounted amount and prints it.

selection = input("Press (1) for Cinema, (2) for Theater : ")
student = input("Are you student(Y/N) : ")
price = 0
#non-discounted fee calculation
if selection == '1':
 price = 10 #cinema
elif selection == '2':
 price = 5 #theatre
#student discount
 if student =='Y' or student =='y':
  price=price / 2 #%50
print(" The fee you have to pay :{}".format(price))

#Program 21
#How to find out if the entered number is Prime or Not on Python?

num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Check for factors from 2 up to num - 1
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break  # Stops the loop immediately once a factor is found
    else:
        # This else belongs to the FOR loop. It runs ONLY if the loop finishes without breaking.
        print(num, "is a prime number")
else:
    # This else belongs to the IF block. It runs if num is 1, 0, or negative.
    print(num, "is not a prime number")

#Program 22
#How to separately find the sum of odd and even numbers up to the number that the user has entered on Python?

NumList = []
Even_Sum = 0
Odd_Sum = 0
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
 value = int(input("Please enter the Value of %d Element : " %i))
NumList.append(value)
for j in range(Number):
 if(NumList[j] % 2 == 0):
  Even_Sum = Even_Sum + NumList[j]
 else:
  Odd_Sum = Odd_Sum + NumList[j]

 print("\nThe Sum of Even Numbers in this List = ", Even_Sum)
 print("The Sum of Odd Numbers in this List = ", Odd_Sum)

#Program 23
#How to calculate the increased salary of the worker whose salary and raise rate is entered on Python?

newsalary = 0 
salary = input("enter new salary : ") 
raise_rate = input("salary raise rate(%) : ") 

# Removed the extra and changed the variable name
newsalary = int(salary) + (int(salary) * int(raise_rate) / 100) 

print("increased salary :", newsalary)


#Program 24
#How to calculate the area and circumference of the circle whose radius is entered using the function on Python.

import math
def find_Diameter(radius):
 return 2 * radius
def find_Circumference(radius):
 return 2 * math.pi * radius
def find_Area(radius):
 return math.pi * radius * radius

 r = float(input(' Please Enter the radius of a circle: '))

 diameter = find_Diameter(r)
 circumference = find_Circumference(r)
 area = find_Area(r)

 print("\n Diameter Of a Circle = %.2f" %diameter)
 print(" Circumference Of a Circle = %.2f" %circumference)
 print(" Area Of a Circle = %.2f" %area)

#Program 25
#How to calculate the area of the rectangle, whose width and height are entered using the function on Python?

def areaRectangle(a, b):
 return (a * b)

 def perimeterRectangle(a, b):
  return (2 * (a + b))
 a = 5;
 b = 6; print ("Area = ", areaRectangle(a, b))

 print ("Perimeter = ", perimeterRectangle(a, b))
#Program 26
#Making a Number Guessing Game with Python

import random
import math

# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between the lower and upper
x = random.randint(lower, upper)
total_chances = round(math.log(upper - lower + 1, 2))
print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < total_chances:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing (Indented inside the while loop)
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses, shows this output.
# (Placed OUTSIDE the while loop)
if count >= total_chances and x != guess:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

#Program 29
#How to check if there is a specified character in a string on Python?

char_list = ["a", "b" ,"c"]
string = "abcd"
matched_list = [characters in char_list for characters in string]
print(matched_list)

 #Line Original sample output
[True, True, True, False]
#Line Python code continued
string_contains_chars = all(matched_list)
print(string_contains_chars)
#Program 30
#How to find the average of odd and even averages of whole numbers on Python?

total = 0
evenSums = 0
oddSums = 0
done = False
while(not done):
 user_in = input("Give me an integer or type 'done' to be done.")
if( user_in.lower() == "done"):
 done = True
else:
# assuming they've typed in an integer
 total += int(user_in)
if user_in % 2 == 0:
 evenSums += user_in
 evenAverage = evenSums / user_in
else:
 oddSums += user_in
 oddAverage = oddSums / user_in
 print(total)
 print("Even Average: " + str(evenAverage))
 print("Odd Average: " + str(oddAverage))