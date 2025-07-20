
# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and print customized reminder
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan for it in your schedule.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task that still needs to be done today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please use high, medium, or low.")

print(f"Reminder: Take a short break!")
