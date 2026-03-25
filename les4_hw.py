"""Exercise 1
Create a list of strings containing words. Using a loop, print out the length
of each word in the list.
words = ["house", "car", "bicycle", "umbrella", "computer"]

Example output:
5
3
7
8
8
"""
words = ["house", "car", "bicycle", "umbrella", "computer"]

for word in words:

    print(len(word))

# ---------------------------------------------------------------------------------------------------------------------

"""Exercise 2
1. Create a list of your favorite fruits. Print the third fruit on the list.
2. Append two new fruits to your favorite fruits. Print the updated list
3. Remove the second fruit from the list and print the updated list.
""" 

fruits = ["Apple", "Mango", "Blueberry", "Peach"]
# Indexing starts at 0, so the 3rd item is index 2
print(fruits[2]) 

# 2. Append two new fruits and print the updated list
fruits.append("Kiwi")
fruits.append("Banane")
print(fruits)

# 3. Remove the second fruit (index 1) and print the updated list
# pop() removes by index; remove() removes by value
fruits.pop(1) 
print(fruits)
# ---------------------------------------------------------------------------------------------------------------------
"""Exercise 3
Write a program that asks the user for their favorite colors (up to 5)
and stores them in a list. Then, create a sentence that says,
"Your favorite colors are: color1, color2, ..." using the .join() function.
"""
# Initialize an empty list to store the favorite colors
favorite_colors = []

# Use a for loop to ask the user up to 5 times
for i in range(5):
    color = input("Please enter a favorite color (or type 'exit' to stop early): ")
    
    # Allow the user to break the loop if they have fewer than 5 favorite colors
    if color == "exit":
        break
        
    # Append the entered color to our list
    favorite_colors.append(color)

# Use the .join() function to combine the list items into a single string separated by commas
joined_colors = ", ".join(favorite_colors)

# Print the final sentence
print(f"Your favorite colors are: {joined_colors}")

# --------------------------------------------------------------------------------------------------------------------

"""Exercise 4
Create a list of even numbers from 2 to 20 (inclusive) using a loop.
Print the list.
"""

