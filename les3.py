# Set the correct password
correct_password = "ABCDE"

# Start an infinite loop
while True:
    # Get input from the user
    user_input = input("Enter password: ")
    
    # Check if the input matches the correct password
    if user_input == correct_password:
        print("Password accepted.")
        break  # This exits the loop immediately
    else:
        print("Incorrect password.")