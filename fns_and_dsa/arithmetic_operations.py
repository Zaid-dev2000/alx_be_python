# Define the perform_operation function with the exact required signature
def perform_operation(num1, num2, operation):
    # Handle the different operations based on the provided parameter
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"  # Return a specific message for division by zero
        return num1 / num2
    else:
        return "Invalid operation"  # Return a message for any unrecognized operation

