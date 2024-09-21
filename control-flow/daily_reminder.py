# Prompt the user to enter a task
task = input("Enter your task: ").strip()

# Prompt for the task's priority level
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate the reminder message using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority level"

# Modify the reminder based on whether the task is time-bound
if priority in ["high", "medium", "low"]:
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

# Ensure the final output starts with "Reminder: "
print(f"Reminder: {reminder}")



