"""Exercise 1:
Extend the program from last week to convert the temperature from Fahrenheit
to Celsius.

1. Ask the user for the name of a city and the current temperature in Fahrenheit.
2. Convert the temperature to Celsius.
3. If the temperature is below freezing point (0 °C),
    print a warning message saying "Alert: The temperature is below freezing point."
Otherwise, print a message saying
    "The temperature is above the freezing point."
4. Lastly, always print the temperature in Celsius (up to one decimal point).

PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9

Example output 1:
Enter the name of a city: Munich
Enter the current temperature in Farenheit: 60
The temperature is above the freezing point.
The current temperature in Munich is 15.6 degrees Celsius."""




city_name = input("Please enter your cityname\n")
current_temperatureF = float(input("Please enter your current_temperatureF\n"))
current_temperatureC = float(current_temperatureF - 32) * 5/9
if current_temperatureC < 0:
    print("Alert:The temperature is below the freezing point.")
else:
    print("The temperature is above the freezing point.")
print (f"The current temperature in {city_name} is {current_temperatureC:.1f} degrees Celsius.")









"""Example output 2:
Enter the name of a city: Munich
Enter the current temperature in Farenheit: 25
Alert: The temperature is below freezing point.
The current temperature in Munich is -3.9 degrees Celsius.
Please enter your cityname
Munich
Please enter your current_temperature
25
Alert:The temperature is below the freezing point.
The current temperature in Munich is -3.9 degrees Celsius."""


# Ask the user for the city name


# Ask the user for the current temperature in Fahrenheit

# Convert the temperature to float


# Convert the temperature to Celsius


# Check if the temperature is below freezing point


# Print the user input in a formatted string"""

"""
Exercise 2:
Now extend the program and ask for the temperature in two cities.

1. Ask the user for the name of two cities and the current temperatures in Fahrenheit.
2. Convert the temperatures to Celsius.
3. If the temperature in both cities is below freezing point (32 °F),
    print a warning message saying "Alert: The temperatures in both cities are below freezing point."
else if the temperature in only one of the cities is below freezing point,
    print a warning message saying "Alert: The temperature in one of the cities is below freezing point."
Otherwise, print a message saying
    "The temperatures in both cities are above the freezing point."
4. Lastly, always print the temperatures in Celsius (up to one decimal point).

PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9""

city_name1 = input("Please enter your cityname1\n")
city_name2 = input("Please enter your cityname2\n")
current_temperature_city1F = float(input("Please enter your current_temperature_city1F\n"))
current_temperature_city2F = float(input("Please enter your current_temperature_city2F\n"))
current_temperature_city1C = float(current_temperature_city1F - 32) * 5/9
current_temperature_city2C = float(current_temperature_city2F - 32) * 5/9
if current_temperature_city1C < 0 and current_temperature_city2C < 0:
    print("Alert: The temperatures in both cities are below freezing point.")
if  current_temperature_city1C < 32 or current_temperature_city2C < 32:
    print("Alert: The temperature in one of the cities are below freezing point.")
else:
    print("The temperatures in both cities are above the freezing point.")
print (f"The current temperature in {city_name1} is {current_temperature_city1C:.1f} degrees Celsius.")
print (f"The current temperature in {city_name2} is {current_temperature_city2C:.1f} degrees Celsius.")


Example output 1 (both cities below freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 15
Please enter the current temperature for Paris in Farenheit: 10
Alert: The temperatures in both cities are below freezing point.
The current temperature in Munich is -9.4 degrees Celsius.
The current temperature in Paris is -12.2 degrees Celsius.


Example output 2 (one city below freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 40
Please enter the current temperature for Paris in Farenheit: 30
Alert: The temperature in one of the cities is below freezing point.
The current temperature in Munich is 4.4 degrees Celsius.
The current temperature in Paris is -1.1 degrees Celsius.


Example output 3 (both cities above freezing point):
Enter the name of the first city: Munich
Enter the name of the second city: Paris
Please enter the current temperature for Munich in Farenheit: 40
Please enter the current temperature for Paris in Farenheit: 50
The temperatures in both cities are above the freezing point.
The current temperature in Munich is 4.4 degrees Celsius.
The current temperature in Paris is 10.0 degrees Celsius."""

# Ask the user for the city names


# Ask the user for the current temperatures in Celsius


# Convert the temperatures to float


# Convert the temperature to Celsius


# Check if the temperature is below freezing point


# Print the user input in a formatted string








