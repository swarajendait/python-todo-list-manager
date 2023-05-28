import os

print("\nWelcome to Todo List Manager!")

# todo list file
list_file = "data/list.txt"

# Check if list file exists, create it if not
if not os.path.isfile(list_file):
    open(list_file, "w").close()

# load todo lists
def loadTodoData():
    with open(list_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            todoListVar, duedate, priorty = line.strip().split(":")
            todoList.append(todoListVar)
            dueDateList.append(duedate)
            priortyList.append(priorty)

loadTodoData()

# write lists, due date, and priorty 
def saveTodoData():
    with open(list_file, "w") as file:
        for todoListVar, duedate, priorty in zip(todoList, dueDateList, priortyList):
            file.write(f"{todoListVar}:{duedate}:{priorty}\n")

# Make lists
todoList = []
dueDateList = []
priortyList = []

def display_tasks():
    pass

def run_tasks():
    print("\n1. Add a task\n2. Delete a task\n3. Mark a task complete\n4. Display all tasks\n5. Exit\n")
    choice = int(input("Please enter the number of the action you want to perform: "))
    if choice == 1:
        todoListVar = input("Enter task: ")
        dueDate = input("Enter Due Date: ")
        priority = int(input("Enter priority (1-5): "))
        todoList.append(todoListVar)
        dueDateList.append(dueDate)
        priortyList.append(priority)
        saveTodoData()
        print("Task added successfully!")
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        quit
    else:
        print("\nError Please try again")
        run_tasks()

run_tasks()