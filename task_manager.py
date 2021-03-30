# Hi Ridhaa. Thank you for the help with this. The call really helped, and while I still struggled a bit, 
# I feel like I've developed a far stronger understanding of everything after this task. Thanks again.

# ========================================================================

# Task management program. 
# Import required modules.
from datetime import datetime, timedelta, date

# Declare initial variables.
nl = '\n'
now = datetime.now()
login = False
login_successful = 'Login successful'
incorrect_username = 'Incorrect username. Please try again.'
incorrect_password = 'Incorrect password. Please try again.'
incorrect_credentials = 'Incorrect credentials. Please try again.'
login_status = 'Incorrect details. Please try again.'

# =================== DEFINE FUNCTIONS USED IN PROGRAM ===================

# Request user credentials.
def get_username():
    return input('Enter username:')

def get_password():
    return input('Enter password:')

# Display main menu and allow user to select option. 
def main_menu():
    print('''
    Please select one of the following options: 
    a - add task
    va - view all tasks
    vm - view my tasks 
    e - exit
    ''')
    response = input('Selection:').strip()
    return response

# Display admin menu that contains additional functionality.
def admin_menu():
    print('''
    Please select one of the following options: 
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks 
    s - view statistics
    gr - generate reports
    e - exit
    ''')
    response = input('Selection:').strip()
    return response

# Register new user. 
def reg_user():
    # Request user input.
    new_username = get_username()
    new_password = get_password()
    count = 0 # Set count to 0

    with open("user.txt", "r+") as users:
        for line in users:
            line = line.split(', ') # Split line in users.txt file by comma
            if new_username == line[0]: # If the username given matches a username in the file, increment count by 1
                count += 1 
            
        if count == 0: # If count is zero, add a new user, because this indicates that the username is not a duplicate. 
            users.write(nl + new_username + ', ' + new_password) # Write username and password to file separated by a comma and space.)
            print("New user successfully created.")
        else:
            print("Username taken. Please try again.")
            reg_user() # Allow user to try again if the username is already taken.

# Create new task.
def add_task():
    # Task details
    task_owner = username
    task_title = input('Task title:')
    task_description = input('Task description:')
    date_assigned = now.strftime("%d %b %Y")
    due_date = input('Due date (please use correct format, e.g. 10 Nov 2021):')
    completion_status = "No"
    
    # Write task details to task file. 
    # Ensure to separate by comma and space as this format is used to extract relevant data from the file when needed.
    open_file = open ('tasks.txt', 'a')
    open_file.write(nl + task_owner + ', ' + task_title + ', ' + task_description + ', ' + date_assigned + ', ' + due_date + ', ' + completion_status)
    open_file.close()
    
    print("New task successfully added.")

# View all tasks on task list
def view_all():
    with open ('tasks.txt') as f: # Open file to access relevant data
        for line in f: 
            data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item. 
            print (f'''
            ====================================================================================================
            Task:\t\t{data[1]}
            Assigned to:\t {data[0]}
            Date assigned:\t{data[3]}
            Due date:\t\t{data[4]}
            Task complete?\t{data[5]}{nl}
            Task description:\t{data[2]}
            ====================================================================================================
            ''')

# View tasks for specific username
def view_mine():
    with open ('tasks.txt') as f: # Open file
        # Print tasks belonging to a particular user.
        for number,line in enumerate(f,1): 
            data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item. 
            if (data[0] == username): # Check for tasks that match the username and print any matches.
                print (f'''
                ================================================================================================
                Task number:\t\t {number}
                Task:\t\t\t{data[1]}
                Assigned to:\t\t {data[0]}
                Date assigned:\t\t{data[3]}
                Due date:\t\t{data[4]}
                Task complete?\t\t{data[5]}{nl}
                Task description:\t{data[2]}
                ================================================================================================
                ''')

        # Request user input to indicate the task they wish to edit or mark as complete.        
        choice = int(input('''
        Please enter the number of the task you wish to edit, or enter -1 to return to the main menu. 
        '''))

    with open ('tasks.txt', "r+") as file: # Open file
        task_list = []
        for number,line in enumerate(file,1):
            if choice == -1:
                Main()
            elif choice == number:
                data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item.
                if data[5].strip() == 'Yes':
                        print('Completed tasks cannot be edited.')
                        exit() # Exit program if task cannot be edited.

                action = int((input('''
                Enter a number to select your action:

                1. Mark task as complete.
                2. Edit task.
                ''')))
                if action == 1: 
                    data[5] = ' Yes' # Change value of 'No' to 'Yes'
                    line = ','.join(data) # Join data in list by a comma
                    task_list.append(line + '\n') # Append task to list
                elif action == 2:
                    if data[5].strip() == 'No':
                        data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item.
                        to_edit = int((input('''
                        Enter a number to select your action:

                        1. Edit user.
                        2. Edit due date.
                        ''')))
                        if to_edit == 1:
                            new_username = input('Please enter updated username:')
                            data[0] = new_username
                            line = ','.join(data) # Join data in list by a comma
                            task_list.append(line) # Append task to list
                            print('Username successfully updated.')
                        elif to_edit == 2:
                            new_date = input('Please enter the new due date using the following format (25 Oct 2019):')
                            data[4] = " " + new_date
                            line = ','.join(data) # Join data in list by a comma
                            task_list.append(line) # Append task to list
                            print('Due date successfully updated.')
            else:
                task_list.append(line) # If task does not have to be changed, append to list to ensure task is not deleted.

    # Write all tasks in task_list to the file. These tasks have been updated, or kept constant if an update was notnecessary.             
    with open ('tasks.txt', "w+") as file: # Open file
        for task in task_list:
            file.write(task)

# Calculate task statistics 
def task_statistics():
    task_count = 0 # Initialise count to 0
    with open ('task_overview.txt') as tasks: # Open task file
        for line in tasks:
            data, value = line.split(': ') 
            task_count = value[0] 
            break # Break from for loop after first iteration because the value needed is contained on the first line
    
    user_count = 0 # Initialise count to 0
    with open ('user_overview.txt') as users: # Open file
        for line in users:
            user_count +=1 # Add to count for each line because each line contains only one user.
    
    # Subtract two users as the first two lines of the user_overview.txt file represent the task and user count. 
    # It is possible to get the task count and user count directly from the user_overview.txt file, although the 
    # instructions request that they be read from task_overview.txt AND user_overview.txt files. 
    print(f"The system contains {task_count} tasks and {user_count - 2} users.")

# Generate reports
def generate_reports():
    # Initialise variables to 0
    total_tasks = 0 
    completed_tasks = 0
    overdue_tasks = 0
    total_users = 0
    user_tasks = 0
    with open ('tasks.txt') as tasks: # Open task file
        for line in tasks:
            total_tasks +=1 # Add to count for each line because each line contains only one task.
            data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item.
            if data[5].strip() == "Yes":
                completed_tasks +=1 # Add to count for each completed task.
            due_date = datetime.strptime(data[4].strip(), '%d %b %Y') # Convert date to datetime object to test whether it has passed.
            current_date = datetime.now()
            if data[5].strip() == "No" and current_date > due_date:
                overdue_tasks += 1
            
    # Calculate task statistics
    uncompleted_tasks = total_tasks - completed_tasks
    percentage_uncompleted = (uncompleted_tasks / total_tasks) * 100 # No rounding done at this stage to maintain full data integrity
    percentage_overdue = (overdue_tasks / total_tasks) * 100 # No rounding done at this stage to maintain full data integrity

    # Write all task information to task_overview.txt file.
    with open('task_overview.txt', 'w') as f:
        f.write('Total tasks: ' + str(total_tasks) + nl + 'Completed tasks: ' + str(completed_tasks) 
        + nl + 'Uncompleted tasks: ' + str(overdue_tasks) + nl + 'Overdue tasks: ' + str(overdue_tasks) 
        + nl + 'Percentage uncompleted: ' + str(percentage_uncompleted) + '%' + nl + 'Percentage overdue: ' + str(percentage_overdue) + '%')
    
    # Display task information in an easy to read manner.
    print(f'''
    ================================================================================================
    Task overview: 

    Total tasks:\t\t {total_tasks}
    Completed tasks:\t\t {completed_tasks}
    Uncompleted tasks:\t\t {uncompleted_tasks}
    Overdue tasks:\t\t {overdue_tasks}
    Percentage uncompleted:\t {percentage_uncompleted:.2f} %
    Percentage overdue:\t\t {percentage_overdue:.2f} %
    ================================================================================================
    ''')

    # Generate User Overview report
    with open ('user.txt') as users: # Open user file
        user_data = []
        for line in users:
            # Initialise variables
            total_users +=1 # Add to count for each line because each line contains one unique user.
            user_tasks = 0
            user_completed = 0
            user_uncompleted = 0
            user_overdue = 0
            user,password = line.split(', ')
            user = user.strip()
            with open('tasks.txt', 'r+') as tasks: # Open task file
                for line in tasks:
                    data = line.split(",") # Split by comma separator: Split a string into a list where each word is a list item.
                    if data[0].strip() == user: # If username in user file matches the user that has been assigned the task.
                        user_tasks +=1
                        user_percentage_of_total = round(((user_tasks / total_tasks) * 100),2)
                        if data[5].strip() == "Yes":
                            user_completed +=1 # Add to count for each completed task.
                            due_date = datetime.strptime(data[4].strip(), '%d %b %Y') # Convert date to datetime object to test whether it has passed.
                            current_date = datetime.now() # For moe information, see the datetime package.
                        if data[5].strip() == "No" and current_date > due_date:
                            user_overdue += 1 
                        # Calculate user specific task statistics
                        user_uncompleted = user_tasks - user_completed
                        user_percentage_completed = (user_completed / user_tasks) * 100
                        user_percentage_uncompleted = (user_uncompleted / user_tasks) * 100
                        user_percentage_overdue = (user_overdue / user_tasks) * 100 
            
            # If the user has no tasks assigned to them, let statistics reflect 0. 
            # This is necessary because if not explicitly stated, the percentages evaluate to 
            # 100% because the system calculates 0/0 = 1. 
            if user_tasks == 0:
                user_percentage_of_total = 0
                user_uncompleted = 0
                user_percentage_completed = 0
                user_percentage_uncompleted = 0
                user_percentage_overdue = 0
            
            # Display task information in an easy to read manner.
            print(f'''
            ================================================================================================
            User overview: 

            User:\t\t\t\t\t {user}
            Total tasks:\t\t\t\t {user_tasks}
            Percentage of total tasks:\t\t\t {user_percentage_of_total:.2f} %
            Percentage completed:\t\t\t {user_percentage_completed:.2f} %
            Percentage uncompleted:\t\t\t {user_percentage_uncompleted:.2f} %
            Percentage overdue:\t\t\t\t {user_percentage_overdue:.2f} %
            ================================================================================================
            ''')

            # Append user statistics to the user_data list
            user_combined = f"{user}, {user_tasks}, {user_percentage_of_total}, {user_percentage_completed}, {user_percentage_uncompleted}, {user_percentage_overdue} {nl}"
            user_data.append(user_combined)
            
    # Write user specific statistics to the user overview file.               
    with open ('user_overview.txt', 'w') as f:
        f.write('Total users: ' + str(total_users) + nl + 'Total tasks: ' + str(total_tasks) + nl) # Include total tasks and total users in file.
        for line in user_data:
            f.write(line) # Write each users statistics to the file.

# Once login evaluates to True, call the admin menu if the user is an admin, and the main menu if not.
# Call the appropriate function based on value returned by the relevant options menu.
def Main():
    if (username == 'admin'): 

        choice = admin_menu()

        if choice == 'vm': # View my tasks.
            view_mine()
        elif choice == 'va': # View all tasks.
            view_all()
        elif choice == 'e': # Exit program.
            exit()
        elif choice == 'a': # Add new task.
            add_task()
        elif choice == 'r': # Register new user.
            reg_user()
        elif choice == 's': # Show statistics
            task_statistics()
        elif choice == 'gr': # Generate reports
            generate_reports()
    else:
        choice = main_menu()

        if choice == 'vm': # View my tasks.
            view_mine()
        elif choice == 'va': # View all tasks.
            view_all()
        elif choice == 'e': # Exit program.
            exit()
        elif choice == 'a': # Add new task.
            add_task()

# ============================= END FUNCTIONS =================================

# Run program.

user_file = open('user.txt', 'r+') # Open user file
login = False # Initialise login value

while login == False: # Continually request user to input credentials until correct
    username = get_username()
    password = get_password()

    for line in user_file: 
        valid_user, valid_password = line.split(", ")
        valid_user = valid_user.strip() # Use list index to get username and strip of any white spaces
        valid_password = valid_password.strip() # Use list index to get password and strip of any white spaces

        if username == valid_user and password == valid_password: # Valid credentials
            login = True
            login_status = login_successful
            Main()
        elif username == valid_user and password != valid_password: # Valid username, invalid password
            login = False
            login_status = incorrect_password
        elif username != valid_user and password == valid_password: # Invalid username, valid password
            login = False
            login_status = incorrect_username
    
    if login == False:
        print(login_status)
    user_file.seek(0) # Return cursor to beginning of file.

user_file.close() # Close user file.

# ==============================================================================