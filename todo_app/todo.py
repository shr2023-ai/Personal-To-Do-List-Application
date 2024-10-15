import json

# Task Class
class Task:
    def _init_(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def _repr_(self):
        return f"Task({self.title}, {self.description}, {self.category}, Completed: {self.completed})"

# File Handling Functions
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task._dict_ for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Main Function for CLI
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))

        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                for idx, task in enumerate(tasks):
                    status = "Completed" if task.completed else "Not Completed"
                    print(f"{idx + 1}. {task.title} - {task.category} ({status})")

        elif choice == '3':
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task.title}")
            task_num = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].mark_completed()

        elif choice == '4':
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task.title}")
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                del tasks[task_num]

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()