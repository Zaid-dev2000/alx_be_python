from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date as "YYYY-MM-DD"
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Call the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
