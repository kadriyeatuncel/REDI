"""Exercise 1

Improve your weather forecast program to handle multiple cities ad more information.

All cities should be stored in a dictionary. The city name should be the key
and the value should be another dictionary containing the following information:
- current temperature in Celsius
- current temperature in Fahrenheit
- is it raining? ("yes" or "no")
- is the sun shining? ("yes" or "no")

The user should be able to finish the program by entering "exit" as city name

Once the user is finished, print a summary for each city with the information above.
If the temperature is below 0°C, print a warning message.
If it is both raining and the sun is shining, print a notification that there is a rainbow.


Example output:
Please enter the name of a city: Munich
Would you like to enter the temperature in Fahrenheit or Celsius?: Celsius
Please enter the current temperature in Celsius in Munich: 14
Is it raining in Munich? (yes/no): no
Is the sun shining in Munich? (yes/no): yes

Please enter the name of a city: Berlin
Would you like to enter the temperature in Fahrenheit or Celsius?: Fahrenheit
Please enter the current temperature in Fahrenheit in Berlin: 34
Is it raining in Berlin? (yes/no): yes
Is the sun shining in Berlin? (yes/no): yes

Please enter the name of a city: Hamburg
Would you like to enter the temperature in Fahrenheit or Celsius?: Celsius
Please enter the current temperature in Celsius in Hamburg: 5
Is it raining in Hamburg? (yes/no): yes
Is the sun shining in Hamburg? (yes/no): no

Please enter the name of a city: exit

Summary:
Munich: 14°C, 57°F, sun and no rain

Berlin: 1°C, 34°F, sun and rain,
Warning: The temperature in Berlin is below the freezing point
There is a rainbow in Berlin.

Hamburg: 5°C, 41°F, no sun and rain
"""
city_list = {}
while True:
    city_name = input("Please enter the name of a city: ")
    if city_name.lower() == "exit":
        break
    temp_unit = input("Would you like to enter the temperature in Fahrenheit or Celsius?: ")
    if temp_unit.lower() == "celsius":
        temp_celsius = float(input(f"Please enter the current temperature in Celsius in {city_name}: "))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
    elif temp_unit.lower() == "fahrenheit":
        temp_fahrenheit = float(input(f"Please enter the current temperature in Fahrenheit in {city_name}: "))
        temp_celsius = (temp_fahrenheit - 32) * 5/9
    else:
        print("Invalid temperature unit. Please enter either 'Celsius' or 'Fahrenheit'.")
        break
    is_raining = input(f"Is it raining in {city_name}? (yes/no): ")
    is_sunny = input(f"Is the sun shining in {city_name}? (yes/no): ")
    
    city_list[city_name] = {
        "temp_celsius": temp_celsius,
        "temp_fahrenheit": temp_fahrenheit,
        "is_raining": is_raining,
        "is_sunny": is_sunny
    }

# Print the summary for each city
print("\nSummary:")
for city, info in city_list.items():
    print(f"{city}: {info['temp_celsius']:.1f}°C, {info['temp_fahrenheit']:.1f}°F, {'sun' if info['is_sunny'] == 'yes' else 'no sun'} and {'rain' if info['is_raining'] == 'yes' else 'no rain'}")
    if info['temp_celsius'] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point.")
    if info['is_raining'] == 'yes' and info['is_sunny'] == 'yes':
        print(f"There is a rainbow in {city}.")
        
"""Exercise 2
Improve your program by  creating two temperature converting functions:
One for converting degrees Celsius to degrees Fahrenheit and one for converting degrees Fahrenheit to degrees Celsius.
Remember the formulas:
Fahrenheit = Celsius * 9 / 5 + 32
Celsius = (Fahrenheit - 32) * 5 / 9

Use the functions in your code every time you need to convert the temperature.
"""
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 1)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 1)


city_list = {}

while True:
    city_name = input("Please enter the name of a city: ")
    
    if city_name.lower() == "exit":
        break

    temp_unit = input("Would you like to enter the temperature in Fahrenheit or Celsius?: ").lower()

    if temp_unit == "celsius":
        temp_celsius = float(input(f"Please enter the current temperature in Celsius in {city_name}: "))
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)

    elif temp_unit == "fahrenheit":
        temp_fahrenheit = float(input(f"Please enter the current temperature in Fahrenheit in {city_name}: "))
        temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

    else:
        print("Invalid temperature unit. Please enter either 'Celsius' or 'Fahrenheit'.")
        continue

    is_raining = input(f"Is it raining in {city_name}? (yes/no): ").lower()
    is_sunny = input(f"Is the sun shining in {city_name}? (yes/no): ").lower()

    city_list[city_name] = {
        "temp_celsius": temp_celsius,
        "temp_fahrenheit": temp_fahrenheit,
        "is_raining": is_raining,
        "is_sunny": is_sunny
    }


print("\nSummary:")

for city, info in city_list.items():
    sun_text = "sun" if info['is_sunny'] == "yes" else "no sun"
    rain_text = "rain" if info['is_raining'] == "yes" else "no rain"

    print(f"{city}: {info['temp_celsius']}°C, {info['temp_fahrenheit']}°F, {sun_text} and {rain_text}")

    if info['temp_celsius'] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point.")

    if info['is_raining'] == "yes" and info['is_sunny'] == "yes":
        print(f"There is a rainbow in {city}.")