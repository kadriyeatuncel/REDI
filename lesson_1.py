# print('hello world')
# Item_1 = int(input("Enter the price of item 1\n"))
# Item_2 = int(input("Enter the price of item 1\n"))
# Item_3 = int(input("Enter the price of item 1\n"))

# total_expenses = int(Item_1 + Item_2 + Item_3)
# print(f"total_expenses equal =  {int(total_expenses)}")
# Average_expence= int(total_expenses/3)
# print(f"total_expenses equal = {Average_expence}")

# dateofBirth = input("Please enter the year of your birth: ")
# Currentyear = input("what is the cureent year")
# age = Currentyear - dateofBirth
# print(fYour)

# print("hello redi\nMy name is Paul")

"""#INPUT
name = input("Please enter your name\n") #input function takes a prompt as argument
surname = input("Please enter your surname\n")
favourite_number = input("Please enter your favourite number\n")
favourite_color = input("Please enter your favourite color\n") 
favourite_song = input("Please enter your favourite song\n")

#PROCESSING (Algorithm)
secure_password = favourite_color + name[1:3] + favourite_number + surname[0:2] + favourite_song

#OUTPUT
print(f"Your secure password is: {secure_password}")"""







"""
Exercise 1:
Create a program that
1. asks the user to enter the name of a city and the current
temperature in Celsius.
2. Store the user input in separate variables and
3. display them.

PS:Use type conversion to ensure that the user's input for the temperature is treated as a float.

Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Celsius in Munich: 25.5
The current temperature in Munich is 25.5 degrees Celsius.


Ask the user for the city name
Ask the user for the current temperature in Celsius
Convert the temperature to float
Print the user input in a formatted string

SOLUTION

city_name = input("Please enter your cityname\n")
current_temperature = float(input("Please enter your current_temperature\n"))
print(f"The current temperature in Munich is {current_temperature} degrees Celsius.")

OUTPUT: The current temperature in Munich is 25.5 degrees Celsius 

Exercise 2:
Now create a program that asks the user to enter the name of two cities and the
current temperatures in each city in Celsius. Store the user inputs in separate
variables (two variables for the names and two for the temperatures) and
display the average temperature.

Example output:
Please enter the name of the first city: Munich
Please enter the name of the second city: Paris
Please enter the current temperature for Munich: 25.5
Please enter the current temperature for Paris: 11.5
The average temperature between Munich and Paris is 18.5 degrees Celsius.


# Ask the user for the city names
# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
# Calculate the average temperature
# Print the user input in a formatted string

firstcity_name = input("Please enter the first city name:\n")
secondcity_name = input("Please enter the second city name:\n")

firstcitycurrent_temperature = float(input(f"Please enter your current temperature in {firstcity_name} in Celsius:\n"))
secondcitycurrent_temperature = float(input(f"Please enter your current temperature in {secondcity_name} in Celsius:\n"))

average_temperature = (firstcitycurrent_temperature + secondcitycurrent_temperature) / 2

print(f"The average temperature between {firstcity_name} and {secondcity_name} is {average_temperature} degrees Celsius.")

LOSUNG:The average temperature between Munich and Paris is 18.5 degrees Celsius. """

"""Exercise 3:
Building upon exercise 2, also convert and print the average temperature in
Fahrenheit. The formula for converting Celsius to Fahrenheit is: F = C * 9/5 + 32.

Example output:
Please enter the name of the first city: Munich
Please enter the name of the second city: Paris
Please enter the current temperature for Munich: 25.5
Please enter the current temperature for Paris: 11.5
The average temperature between Munich and Paris is 18.5 degrees Celsius.
That's 65.3 degrees Fahrenheit. 


# Ask the user for the city names

# Ask the user for the current temperatures in Celsius

# Convert the temperatures to float

# Calculate the average temperature

# Print the user input in a formatted string

# Convert the average temperature to Fahrenhei

firstcity_name = input("Please enter the first city name:\n")
secondcity_name = input("Please enter the second city name:\n")

firstcitycurrent_temperature = float(input(f"Please enter your current temperature in {firstcity_name} in Celsius:\n"))
secondcitycurrent_temperature = float(input(f"Please enter your current temperature in {secondcity_name} in Celsius:\n"))

average_temperature = (firstcitycurrent_temperature + secondcitycurrent_temperature) / 2
average_temperature_Fahrenheit = (average_temperature * 9/5) + 32

print(f"The average temperature between {firstcity_name} and {secondcity_name} is {average_temperature} degrees Celsius.\n"
       f"That's {average_temperature_Fahrenheit} degrees Fahrenheit.")""

       # Prompt the user to enter two numbers
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

Compare the two numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is not greater than {num2}.")""
    