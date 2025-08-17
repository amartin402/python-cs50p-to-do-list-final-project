# Python Daily To Do List Application
## How to Use the Application:
#### Video Demo: https://youtu.be/L603igKQ8u8
## Description:
#### Project:
The project is a Python written console application that stores added "to do" tasks in a CSV file. On the first startup of the application it will create a csv file to store the tasks that the user logs. Once the user has logged a few tasks that are incomplete, on future startups of the application it will first display the incomplete tasks in a grid view before the selection menu.

Being my first full real Python application, creating the project has been fun and rewarding. Dealing with scenarios of how to logically make functions work and using the fundamental basics of the Python language.

In future I would like to enhance this project, and build a web-based application that uses a sqlite database to store the data. This has been a great journey with CS50P! "Hello World" and Thank you David J. Malan!

#### Project contains and does:
* The project only contains one python file that is named project.py
* Additional libraries used
  * tabulate 0.9.0
    * `pip install tabulate`
* Functions(fn) within the file:
  *  file_exists (filename)
     *  The fn checks to see if a csv file exists. If the file does not exist it will create one. It takes in a filename attribute used for naming the csv file.
  *  menu()
     *  Prints the feature options and validates if the selected option exists.
  *  load(filename, headers, data)
     *  The fn loads the menu() fn which supplies the chosen_option() fn with a validate option. It takes in a filename attribute, headers attribute and data object(list dictionary) for the chosen_option fn to use.
  *  chosen_option(option, filename, headers, data)
     *  The fn takes in the option attribute, filename attribute, headers attribute and data object to action the correct option.
  *  add(row_id)
     *  The fn gets and validates the user's input for a to do task entry. It takes in a row_id attribute to add to the row_id integer for that record.
  *  remove(all_data)
     *  The fn gets and validates the user's input for a row that he/she would like to remove from the data. It takes in a data object and returns new data object without the row that is removed.
  *  display(data, output=0)
     *  The fn displays the data object in a grid output. It takes in a data object and an output attribute that define whether the output should have a title or not.
  *  search(all_data)
     *  The fn gets and validates the user's input for a correct due date. It takes in a data object and returns a filtered data object.
  *  complete(all_data, incomplete)
     *  The fn gets and validates the user's input of the row id. It takes in two data objects, one a full set of the information and the other been the incomplete tasks. It outputs the altered data set with the changes.
  *  reminder(data, column_name)
     *  The fn takes in a data object and the specified column name that is in the data set. It returns a data object with all the incomplete tasks.
  *  reader(filename, headers)
     *  The fn readers a csv file and returns a data object. Takes in a filename attribute and headers attribute for the csv file it reads.
  *  writer(filename, headers, data)
     *  The fn appends a row of data to a csv file. Takes in a filename attribute, headers attribute and data object for the csv file it appends to.
  *  rewriter(filename, headers, data)
     *  The fn rewrites the rows of data to a csv file. Takes in a filename attribute, headers attribute and data object for the csv file it writes to.
  *  get_max_id(data, column_name)
     *  The fn returns the maximum row id for a data set. Takes in a data object and the specific column name attribute used to identify the integer column to get the maximum id.

## The application has the following features:
* 1) Add a task:
  * The user is able to add their task to a csv file.
* 2) Remove a task:
  * The user is able to remove a task from the csv file.
* 3) View all tasks:
  * The user is able to view all logged tasks in the csv file.
* 4) Search tasks by due date:
  * The user is able to search for tasks entering a date.
* 5) Set a task as complete:
  * The user can set incomplete tasks as complete.
* 6) Exit application
  * The user can exit the application.

