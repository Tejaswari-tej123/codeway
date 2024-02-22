class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if 0 <= task_index < len(self.tasks):
                del self.tasks[task_index]
                print("Task removed successfully!")
            else:
                print("Invalid task index!")
        except ValueError:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            remove_task(todo_list)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select again.")

def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.add_task(task)

def remove_task(todo_list):
    task_index = input("Enter task index to remove: ")
    todo_list.remove_task(task_index)

if __name__ == "__main__":
    main()
