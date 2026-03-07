"""
Exercise 5: Grade Classification
Instruction:

Ask the user to enter a numeric grade (0 to 100) using input().
Convert the input to an integer and classify the grade as follows:
90 or above: "A"
80 to 89: "B"
70 to 79: "C"
60 to 69: "D"
Below 60: "F"
Print the grade classification.
"""
grade = int(input("Enter your numeric grade (0 to 100): "))

if grade >= 90:
    print ("A")
elif grade >= 80:
    print ("B")
elif grade >= 70:
    print ("C")
elif grade >= 60:
    print ("D")
else:
   print ("F")

"""
Exercise 6: Ticket Price
Instruction:

Ask the user to enter their age using input().
Convert the input to an integer and determine the ticket price based on age:
0 to 3 years: Free
4 to 12 years: $10
13 to 64 years: $15
65 and above: $5
Print the ticket price.

"""
age = int(input("Enter your age: "))
if age < 3:
    print ("Free")
elif age >= 4 and age <= 12:
    print ("$10")
elif age >= 13 and age<=64:
    print ("$15")
else :
    print ("$5")

"""

Exercise 7: Logical Combinations
Instruction:

Ask the user to enter an integer using input().
Convert the input to an integer and check if it's between 10 and 50 (inclusive) or less than 0.
Print the result of the condition."""

integer = int(input("enter an integer: "))
if integer >=10 and integer <=50 or integer < 0:
    print ("it's between 10 and 50 or less than 0.")
else :
    print ("it's NOT between 10 and 50 or less than 0.")

"""
Exercise 8:
Enhance the code below, so that when a user wants anything else besides coffee or tea you inform the user 
that the required beverage is not available:
print("Turning on the machine...")
beverage = input("Do you want tea or coffee? ")
if beverage == "tea":
    print("Preparing tea...")
elif beverage == "coffee" :
    print("Preparing coffee...")
print("Turning off the machine.")
"""
print("Turning on the machine...")
beverage = input("Do you want tea or coffee? ")
if beverage == "tea":
    print("Preparing tea...")
elif beverage == "coffee" :
    print("Preparing coffee...")
else :
    print("Turning off the machine.")

