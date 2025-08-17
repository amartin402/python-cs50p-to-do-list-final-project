import sys
from datetime import date, datetime
import csv
import tabulate

def main():
    filename = 'tasks.csv'
    headers = ['row_id','task_create_date','task_description','task_due_date','task_complete']
    print(r'''
         ____    _    ___ _  __   __  _____ ___    ____   ___    _     ___ ____ _____
        |  _ \  / \  |_ _| | \ \ / / |_   _/ _ \  |  _ \ / _ \  | |   |_ _/ ___|_   _|
        | | | |/ _ \  | || |  \ V /    | || | | | | | | | | | | | |    | |\___ \ | |
        | |_| / ___ \ | || |___| |     | || |_| | | |_| | |_| | | |___ | | ___) || |
        |____/_/   \_\___|_____|_|     |_| \___/  |____/ \___/  |_____|___|____/ |_|
        ''')
    file_exists(filename)
    data = reader(filename, headers)
    if len(data) > 0:
        incomplete = reminder(data, 'task_complete')
        if len(incomplete) > 0:
            display(incomplete)
    load(filename, headers, data)

def file_exists(filename):
    try:
        with open(filename, 'r') as file:
            pass
    except FileNotFoundError:
        with open(filename, 'w') as file:
            pass

def menu():
    options = [1,2,3,4,5,6]
    print('''Please choose the action you would like to do:\n
1 Add a task
2 Remove a task
3 View all tasks
4 Search tasks by due date
5 Set a task as complete
6 Exit application
                    ''')
    while True:
        try:
            option = int(input("Add your number selection here and press enter: "))
            if option not in options:
                print("\nOnly allowed to choose a number from the menu.\n")
                continue
            return option
        except ValueError:
            print("\nYou must enter an integer number from the selection menu.\n")

def chosen_option(option, filename, headers, data):
    if option == 1:
        next_id = 1
        next_id += get_max_id(data, 'row_id')
        row = add(next_id)
        writer(filename, headers, row)
        new_data = reader(filename, headers)
        display(new_data, 1)
        load(filename, headers, new_data)
    if option == 2:
        all_data = reader(filename, headers)
        if len(all_data) > 0:
            print("\nBelow are all the tasks: ")
            display(all_data)
            new_data = remove(all_data)
            rewriter(filename, headers, new_data)
            display(new_data, 1)
            load(filename, headers, new_data)
        else:
            print("\nThere are no tasks to be removed.\n")
            load(filename, headers, all_data)
    if option == 3:
        all_data = reader(filename, headers)
        display(all_data, 1)
        load(filename, headers, all_data)
    if option == 4:
        all_data = reader(filename, headers)
        search_data = search(all_data)
        if len(search_data) > 0:
            display(search_data, 1)
        else:
            print("\nNo rows returned.\n")
        load(filename, headers, all_data)
    if option == 5:
        all_data = reader(filename, headers)
        incomplete = reminder(all_data, 'task_complete')
        if len(incomplete) > 0:
            print("\nBelow are all the incomplete tasks: ")
            display(incomplete)
            new_data = complete(all_data, incomplete)
            rewriter(filename, headers, new_data)
            display(new_data, 1)
            load(filename, headers, new_data)
        else:
            print("\nThere are no tasks to be set as complete.\n")
            load(filename, headers, all_data)
    if option == 6:
        exit()

def add(row_id):
    while True:
        try:
            task_due_date = datetime.strptime(input("\nEnter task due date(YYY-MM-DD) and press enter: "),"%Y-%m-%d").date()
            task_create_date = date.today()
            if task_due_date < task_create_date:
                print("\nThe task's due date is smaller than the task's create date.")
                continue
            task_description = input("Enter task description: ")
            break
        except ValueError:
            print("\nDue date is not in the correct format, YYYY-MM-DD")
    return [{'row_id': row_id,'task_create_date': task_create_date,'task_description': task_description,'task_due_date': task_due_date, 'task_complete': 0}]

def remove(all_data):
        list_row_id = []
        for row in all_data:
            list_row_id.append(int(row['row_id']))
        while True:
            try:
                task_to_remove = int(input("Enter the task's row id that you would like to remove: "))
                if task_to_remove not in list_row_id:
                    print("\nYou can only enter row id's that are in the tasks table.")
                    continue
                break
            except ValueError:
                print("\nYou must enter an integer row id number from the incomplete tasks table.")
        new_data = []
        new_row_id = 1
        for row in all_data:
            if int(row['row_id']) != task_to_remove:
                row['row_id'] = new_row_id
                new_data.append(row)
                new_row_id += 1
        return new_data

def search(all_data):
    while True:
        try:
            task_due_date = datetime.strptime(input("\nEnter task due date(YYY-MM-DD) and press enter: "),"%Y-%m-%d").date()
            break
        except ValueError:
            print("\nDate is not in the correct format, YYYY-MM-DD")
    search_data = []
    for row in all_data:
        if datetime.strptime(row['task_due_date'],'%Y-%m-%d').date() >= task_due_date:
            search_data.append(row)
    return search_data

def complete(all_data, incomplete):
    list_row_id = []
    for row in incomplete:
        list_row_id.append(int(row['row_id']))
    while True:
        try:
            row_id = int(input("Enter the task's row id that you would like to set as complete and press enter: "))
            if row_id not in list_row_id:
                print("\nYou can only enter row id's that are in the incomplete tasks table.\n")
                continue
            break
        except ValueError:
            print("\nYou must enter an integer row id number from the incomplete tasks table.\n")
    # set task incomplete section
    for row in all_data:
        if int(row['row_id']) == row_id:
            row['task_complete'] = 1
    return all_data

def load(filename, headers, data):
    option = menu()
    chosen_option(option, filename, headers, data)

def reminder(data, column_name):
    incomplete = []
    counter = 0
    for row in data:
        if int(row[column_name]) == 0:
            counter += 1
            incomplete.append(row)
    return incomplete

def display(data, output=0):
    if len(data) > 0:
        if output == 1:
            print("\nOutput\n" + tabulate.tabulate(data,headers='keys',tablefmt="grid") + "\n")
        else:
            print(tabulate.tabulate(data,headers='keys',tablefmt="grid") + "\n")
    else:
        print("\nNo rows returned.\n")

def reader(filename, headers):
    try:
        with open(filename,'r') as file:
            reader = csv.DictReader(file,fieldnames=headers)
            data = list(reader)
    except:
        raise sys.exit("File not found.")
    return data

def writer(filename, headers, data):
    if len(data) > 0:
        try:
            with open(filename,'a') as file:
                _writer = csv.DictWriter(file,fieldnames=headers)
                _writer.writerows(data)
        except:
            raise sys.exit("Unable to write to file.")
    else:
        sys.exit("No data available to write to file.")

def rewriter(filename, headers, data):
    if len(data) > 0:
        try:
            with open(filename,'w') as file:
                _writer = csv.DictWriter(file,fieldnames=headers)
                _writer.writerows(data)
        except:
            raise sys.exit("Unable to write to file.")
    else:
        sys.exit("No data available to write to file.")

def get_max_id(data, column_name):
    max_id = 0
    for row in data:
        if int(row[column_name]) > max_id:
            max_id = int(row[column_name])
    return max_id

def exit():
    sys.exit()

if __name__ == "__main__":
    main()
