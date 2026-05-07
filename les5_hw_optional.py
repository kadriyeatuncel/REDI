# DICTIONARIES
"""Exercise 1
Create a list of dictionary items, where each dictionary represents a book with
keys like "title", "author", and "year". Print the details of all books.

Example output:
Title: The Hitchhiker's Guide to the Galaxy. By Douglas Adams. Published in 1979.
Title: The Great Gatsby. By F. Scott Fitzgerald. Published in 1925.
"""


books = [
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

for book in books:
    print(f"Title: {book['title']}. By {book['author']}. Published in {book['year']}.")

"""Exercise 2

Write a program that simulates a simple inventory system. Create a dictionary
with items as keys and their quantities as values. Allow the user to "buy"
items by reducing the quantity, and print the updated inventory after each
purchase.

inventory = {
    "apple": 5,
    "banana": 3,
    "orange": 2,
    "pear": 1
}
Example output:
Please enter the name of an item to buy: apple
There are 4 apples left in stock.
Please enter the name of an item to buy: pear
There are 0 pears left in stock.
Please enter the name of an item to buy: pear
Sorry, there are no pears left in stock.
Please enter the name of an item to buy: exit
"""
# Initial inventory dictionary
inventory = {
    "apple": 5,
    "banana": 3,
    "orange": 2,
    "pear": 1
}

while True:
    # Ask the user for the item name
    item = input("\nPlease enter the name of an item to buy (or 'exit' to quit): ").strip().lower()

    # Check if the user wants to exit
    if item == "exit":
        break

    # Check if the item exists in the inventory
    if item in inventory:
        # Check if there is enough stock
        if inventory[item] > 0:
            # Reduce the quantity by 1
            inventory[item] -= 1
            print(f"There are {inventory[item]} {item}s left in stock.")
        else:
            # Case when quantity is zero
            print(f"Sorry, there are no {item}s left in stock.")
    else:
        # Case when the item is not sold in this store
        print(f"We do not have {item} in our inventory.")

print("\nFinal Inventory Status:")
print(inventory)

# FUNCTIONS
"""Exercise 1
Simple Calculator: Write a function that takes two numbers and an operator
(+, -, *, /) as input from the user and returns the result of the operation.
"""
def simple_calculator():
    # Get user input for numbers and the desired operator
    # We use float() to allow decimal numbers like 5.5
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()

    # Perform the calculation based on the selected operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Check to prevent division by zero errors
        if num2 != 0:
            result = (num1 / num2)
            result = f"{result:.2f}"
        else:
            return "Error: Division by zero is not allowed."
    else:
        # Handle cases where the user enters an unsupported operator
        return "Error: Invalid operator."

    # Return the formatted string showing the calculation and result
    return f"The result of {num1} {operator} {num2} is: {result}"

# Example of how to call the function:
(simple_calculator())

"""Exercise 2
Area Calculator: Define functions for calculating the area of a circle, square, and triangle. 
Prompt the user to choose a shape and input the necessary parameters to calculate and 
display the area.
The area of a circle is calculated as follows:
area = pi * radius * radius
The area of a square is calculated as follows:
area = length * length
The area of a triangle is calculated as follows:
area = 0.5 * base * height
"""
def area_calculator():
    import math

    # Prompt the user to choose a shape
    shape = input("Choose a shape to calculate the area (circle, square, triangle): ").strip().lower()

    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius * radius
        return f"The area of the circle with radius {radius} is: {area:.2f}"

    elif shape == "square":
        length = float(input("Enter the length of the square: "))
        area = length * length
        return f"The area of the square with length {length} is: {area:.2f}"

    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        return f"The area of the triangle with base {base} and height {height} is: {area:.2f}"

    else:
        return "Error: Invalid shape selected."
# Example of how to call the function:
(area_calculator())

"""Exercise 3
List Manipulation: Create a function that takes a list of numbers as input and
returns a new list containing only the even numbers from the original list.
"""
def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
# Example of how to call the function:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_numbers(numbers_list))

"""Exercise 4
Prime Number Checker: Create a function that takes an integer as input and checks
whether it's a prime number or not. Print a message indicating whether
the number is prime.

Remember, a prime number is a number that is only divisible by 1 and itself.
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example of how to call the function:
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    