my_file = open("tasklist.txt", "+w")
def option1():
    print(taskList)
def option2():
    add1 = input("What would you like to add?")
    taskList.append(add1)
    print(taskList)
def option3():
    delete1 = int(input("Which number would you like to delete?"))
    delete1 = delete1-1
    print("Item has been deleted.")
def option4():
    print("Please make another selection")
taskList= []
def listToDo():
    print("Congratulations! You're running Cody's Task List program.")
    answer1 = input("What would you like to do next? \n \n 1)List all tasks: \n 2)Add a new task: \n 3)Delete a task: \n 4)type q or quit to leave\n")
    my_file.seek(0)
    while ((answer1 != "q") and (answer1 != "quit")):
        if (answer1 == "List" or answer1 == "list" or answer1 == "1"):
            option1()
        elif (answer1 == "add" or answer1 == "2"):
            option2()
        elif (answer1 == "delete" or answer1 == "Delete" or answer1 == "3"):
            option3()
        else:
            option4()
        answer1 = input("What would you like to do next?")
    answer2 = input("Would you like to save your list?")
    if (answer2 == "Yes" or answer2 == "yes" or answer2 == "y"):
        my_file.write(str(taskList))
    else:
        print("Hope you remember the list!")

listToDo()
#i input("What would you like to do next?")

