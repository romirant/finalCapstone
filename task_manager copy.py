# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


# Create empty task list and create task dictionary
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Functions====

# a function that is called when the user selects ‘r’ to register a user.
def reg_user():
    '''Add a new user to the user.txt file'''

    while True:
        # - Request input of a new username
        new_username = input("New Username: ")

        # Check if the new username already exists
        if new_username in username_password.keys():
            print("Username already exists. Please try a different username.")
        else:
            break

    while True:
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
                break

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")


# a function that is called when a user selects ‘a’ to add a new task.
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''

    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.
        '''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")
        break


# a function that is called to update the tasks.txt file.
def write_to_tasks_file():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


# a function that is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’.
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


# a function that is called when users type ‘vm’ to view all the tasks that have been assigned to them.
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    '''

    while True:
        for i, t in enumerate(task_list):
            if t['username'] == curr_user:
                disp_str = f"Task Number: {i + 1}\n"
                disp_str += f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)

        task_choice = input("Enter the task number to select a task (or -1 to return to the main menu): ")

        # Exits back to main menu loop
        if task_choice == '-1':
            break

        # Checks user input is not an invalid number
        try:
            task_choice = int(task_choice)
            if task_choice < 1 or task_choice > len(task_list):
                print("Invalid task number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        selected_task = task_list[task_choice - 1]

        complete_choice = input("Do you want to mark this task as complete? (Yes/No): ")

        # Writes to the tasks.txt file to update the user changes
        if complete_choice.lower() == 'yes' and selected_task['completed'] != 'Yes':
            selected_task['completed'] = 'Yes'
            print("Task marked as complete!")
            write_to_tasks_file()

        elif selected_task['completed'] == 'Yes':
            print("This task has already been completed and cannot be edited.")

        elif complete_choice.lower() == 'no' and selected_task['completed'] != 'Yes':

            edit_choice = input("Do you want to edit the assigned username or the due date? (or -1 to return to the main menu) (Username/Due Date): ")

            # Exits back to main menu loop
            if edit_choice == '-1':
                break

            elif edit_choice.lower() == 'username':

                while True:
                    new_username = input("Enter the new username: ")
                    
                    # Checks to see if new username is in the username_password dictionary
                    if new_username not in username_password.keys():
                        print("User does not exist. Please enter a valid username")

                    # Writes to the tasks.txt file to update the user changes
                    else:
                        selected_task['username'] = new_username
                        print("Username updated successfully!")
                        write_to_tasks_file()
                        break

            # Writes to the tasks.txt file to update the user changes
            elif edit_choice.lower() == 'due date':
                new_due_date = input("Enter the new due date (format: YYYY-MM-DD): ")
                try:
                    new_due_date = datetime.strptime(new_due_date, '%Y-%m-%d')
                    selected_task['due_date'] = new_due_date
                    print("Due date updated successfully!")
                    write_to_tasks_file()

                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

            else:
                print("Invalid input. Please choose either 'Username' or 'Due Date'.")


# Two functions that are called when users type ‘gr’ to output two reports that print data on all tasks.
def generate_task_overview_report():
    """Generates a user overview report based on the user data and task list.
    """
    # Sets report values as 0 and then iterates over the data to produce the percentages
    total_tasks = len(task_list)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    for t in task_list:
        if t['completed'] is True:
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            due_date = datetime.combine(t['due_date'], datetime.min.time())
            if due_date < datetime.combine(date.today(), datetime.min.time()):
                overdue_tasks += 1

    # Defensive coding to prevent division by zero
    if total_tasks > 0:
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100
    else:
        incomplete_percentage = 0
        overdue_percentage = 0

    report = "Task Overview Report\n"
    report += f"Total tasks: {total_tasks}\n"
    report += f"Completed tasks: {completed_tasks}\n"
    report += f"Uncompleted tasks: {uncompleted_tasks}\n"
    report += f"Overdue tasks: {overdue_tasks}\n"
    report += f"Incomplete tasks percentage: {incomplete_percentage:.2f}%\n"
    report += f"Overdue tasks percentage: {overdue_percentage:.2f}%\n"

    with open("task_overview.txt", "w") as file:
        file.write(report)

    print(report)
    print("\nTask overview report generated successfully!")


def generate_user_overview_report():
    """Generates a user overview report based on the user data and task list.
    """
    total_users = len(user_data)
    total_tasks = len(task_list)

    report = "User Overview Report\n"
    report += f"Total users: {total_users}\n"
    report += f"Total tasks: {total_tasks}\n"

    # Sets report values as 0 and then iterates over the data to produce the percentages
    for user_data_entry in user_data:
        usernames = user_data_entry.split(';')[0]
        assigned_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0

        for t in task_list:
            if t['username'] == usernames:
                assigned_tasks += 1
                if t['completed'] is True:
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    due_date = datetime.combine(t['due_date'], datetime.min.time())
                    if due_date < datetime.combine(date.today(), datetime.min.time()):
                        overdue_tasks += 1

        # Defensive coding to prevent division by zero
        if assigned_tasks and total_tasks > 0:
            assigned_percentage = (assigned_tasks / total_tasks) * 100
            completed_percentage = (completed_tasks / assigned_tasks) * 100
            uncompleted_percentage = (uncompleted_tasks / assigned_tasks) * 100
            overdue_percentage = (overdue_tasks / assigned_tasks) * 100
        
        else:
            assigned_percentage = 0
            completed_percentage = 0
            uncompleted_percentage = 0
            overdue_percentage = 0

        report += f"\nUser: {usernames}\n"
        report += f"Assigned tasks: {assigned_tasks}\n"
        report += f"Percentage of total tasks assigned: {assigned_percentage:.2f}%\n"
        report += f"Percentage of assigned tasks completed: {completed_percentage:.2f}%\n"
        report += f"Percentage of assigned tasks uncompleted: {uncompleted_percentage:.2f}%\n"
        report += f"Percentage of assigned tasks overdue: {overdue_percentage:.2f}%\n"

    with open("user_overview.txt", "w") as file:
        file.write(report)

    print(report)
    print("\nUser overview report generated successfully!")


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # Calls function to register a new user
    if menu == 'r':
        reg_user()

    # Calls function to add a task
    elif menu == 'a':
        add_task()

    # Calls function to view all tasks
    elif menu == 'va':
        view_all()

    # Calls function to view all of curr_user's tasks and allows editing of tasks
    elif menu == 'vm':
        view_mine()

    # Calls two functions that gather information about users and tasks and prints out the stats
    elif menu == 'gr':
        generate_task_overview_report()
        generate_user_overview_report()

    # Allows the admin to print out basic stats and calls the info from tasks.txt and user.txt
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users and tasks.'''
        if not os.path.exists('tasks.txt') or not os.path.exists('user.txt'):
        
        # Generate the text files if they don't exist
            with open('tasks.txt', 'w') as tasks_file, open('user.txt', 'w') as user_file:
                pass

        # Will read the contents of the text files
        with open('tasks.txt', 'r') as tasks_file, open('user.txt', 'r') as user_file:
            tasks_data = tasks_file.read()
            users_data = user_file.read()

        # Display the reports
        print("-----------------------------------")
        print("Statistics Report")
        print("-----------------------------------")
        print(f"Number of users: \t\t {len(users_data.splitlines())}")
        print(f"Number of tasks: \t\t {len(tasks_data.splitlines())}")
        print("-----------------------------------")

    # Quits the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Defensive programming for an incorrect user input
    else:
        print("You have made a wrong choice, Please Try again")
