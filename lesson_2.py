"""num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is not greater than {num2}.") """


"""name = str(input("Enter your name: "))
if len(name) >= 6:
    print("You have a long name.")
else:
    print("Your name is shorter than 6 characters.")"""

# Prompt the user to enter a numeric grade
grade = int(input("Enter your numeric grade (0 to 100): "))

# Classify the grade
if grade >= 90:
    classification = "A"
elif grade >= 80:
    classification = "B"
elif grade >= 70:
    classification = "C"
elif grade >= 60:
    classification = "D"
else:
    classification = "F"

# Print the grade classification
print(f"Your grade classification is: {classification}")
