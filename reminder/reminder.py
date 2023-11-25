# Moein Moatali

import datetime
import time

# Function to take user input for date, time, and task
def get_user_input():
    date_input = input("Enter the date (YYYY-MM-DD): ")
    time_input = input("Enter the time (HH:MM): ")
    task_input = input("Enter the task: ")
    return date_input, time_input, task_input

# Function to convert user input to datetime object
def convert_to_datetime(date_str, time_str):
    date_time_str = date_str + ' ' + time_str
    return datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

# Function to check and remind the user
def remind_user(date_time, task):
    while True:
        current_time = datetime.datetime.now()
        if current_time >= date_time:
            print(f"It's time to {task}!")
            break
        time.sleep(60)  # Check every minute

# Get user input
user_date, user_time, user_task = get_user_input()

# Convert user input to datetime object
reminder_datetime = convert_to_datetime(user_date, user_time)

# Remind the user at the specified time
remind_user(reminder_datetime, user_task)




