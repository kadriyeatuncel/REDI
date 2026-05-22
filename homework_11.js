// 1. Define the required variables
let sum = 0;          // To store the total sum
let numbers = 0;      // Counter for the number of inputs
let average = 0;      // To store the calculated average

// 2. Take initial input from the user
let user_input = parseInt(prompt("Please enter a number: (Negative number stops input)"));

// 3. Do a while loop to run until the user input is < 0
while (user_input >= 0) {
    
    // Add all positive numbers
    sum += user_input; 

    // Increase loop counter
    numbers++;

    // Take input again if the number is positive (inside while loop)
    user_input = parseInt(prompt("Please enter a number:"));
}

// 4. Calculate average (Check if numbers > 0 to avoid division by zero)
if (numbers > 0) {
    average = sum / numbers;
} else {
    average = 0;
}

// 5. Output into console
console.log("Number of inputs: ", numbers, "Sum: ", sum, "Average: ", average);
console.log(`The sum of all inputs is: ${sum} !`);
console.log(`The average of all inputs is: ${average} !`);