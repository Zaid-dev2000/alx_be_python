# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
