def calculate_factorial(n):
    # Initialize the factorial variable to 1
    factorial = 1
    
    # Calculate the factorial using a for loop
    for i in range(1, n + 1):
        factorial *= i
    
    # Return the computed factorial
    return factorial

# an Example  of the calculate_factorial function
num = 6
result = calculate_factorial(num)
print(f"The factorial of {num} is {result}")
