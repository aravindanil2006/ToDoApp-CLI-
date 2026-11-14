user_input = 'rand'
task = []
def Menu():
    print("\n----CLI ToDo List App----")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. Exit")

while user_input != '3':
    Menu()
    user_input = input("Enter Your Choice: ")
    if user_input == '1':
        data = input("What is the Task need to be Added: ")
        task.append(data)
        print("\n--Current Tasks--\n")
        for i in task:
            print(" -",i)
    if user_input == '2':
        datarm = input("What is the Task need to be Removed: ")
        if datarm in task:
            task.remove(datarm)
            print("\n--Current Tasks--\n")
            for i in task:
                print(" -",i)
    if user_input == '3':
        print("Thank You!")
