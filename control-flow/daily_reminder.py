task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority :
    case "high" :
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. You can schedule it when convenient.")
    case "medium" :
        if time_bound.lower() =="yes":
            print(f"Reminder: {task} is a medium priority task that should be done soon!")
        else:
            print(f"Note: {task} is a medium task. Complete it when free .")
    case "low":
        if time_bound.lower() == "yes":
             print(f"Note: {task} is a low priority task. Consider complating it when you have free time.")
        else:
            print(f"Note: {task} is a medium task. Complete it when free .")
    case _:
        print(f"{task} is not recognized.")
           