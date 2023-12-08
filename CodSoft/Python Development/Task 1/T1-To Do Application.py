class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class ToDo:
    def __init__(self):
        self.tasks = []

    def Create(self, name, description):
        new_task = Task(name, description)
        self.tasks.append(new_task)
        print(f"\nTask '{name}' created.")

    def List(self):
        if not self.tasks:
            print("\nNo tasks available.")
        else:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task.completed else "Pending"
                print(f"{index}. {task.name} - {task.description} - Status: {status}")

    def Completed(self, task_index):
        if task_index >= 1 and task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f"Task '{task.name}' marked as completed.")
        else:
            print("\nInvalid task index.")

todo = ToDo()

while True:
    print("\n==== ToDo Application ====\n")
    print("1. Create Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("\nEnter choice: \n")

    if choice == '1':
        name = input("\nEnter task name: ")
        description = input("\nEnter task description: ")
        todo.Create(name, description)
    elif choice == '2':
        todo.List()
    elif choice == '3':
        todo.List()
        task_index = int(input("\nEnter the index of the task to mark as completed: "))
        todo.Completed(task_index)
    elif choice == '4':
        print("\nExiting ToDo Application.")
        break
    else:
        print("\nInvalid choice. Please enter a valid option.")
