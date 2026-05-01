from storage import load_tasks, save_tasks
from task import Task
from datetime import datetime

def get_valid_task_id(tasks, action):
    if not tasks:
        print("No tasks available.")
        return None

    try:
        task_id = int(input(f"Enter task ID to {action}: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    for task in tasks:
        if task.id == task_id:
            return task

    print("Task not found.")
    return None

def main():
    tasks = load_tasks()

    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        
        elif choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue
            
            priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()

            if priority not in ["Low", "Medium", "High"]:
                print("Invalid priority. Defaulting to Low.")
                priority = "Low"

            due_date = input("Enter due date (YYYY-MM-DD) or leave empty: ").strip()

            if due_date == "":
                due_date = None
            
            if due_date:
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Setting due date to None.")
                    due_date = None

            if tasks:
                task_id = max(task.id for task in tasks) + 1
            else:
                task_id = 1
            
            new_task = Task(task_id, title, priority=priority, due_date=due_date)

            tasks.append(new_task)
            print("Task added successfully.")
            save_tasks(tasks)
        
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue

            print("\nYour Tasks:")

            priority_order = {"High": 3, "Medium": 2, "Low": 1}

            sorted_tasks = sorted(
                tasks,
                key=lambda task: (
                    task.completed,
                    -priority_order.get(task.priority, 1),
                    task.due_date if task.due_date else "9999-12-31"
                )
            )

            for task in sorted_tasks:
                status = "✓" if task.completed else "✗"
                due = task.due_date if task.due_date else "No due date"
                print(f"{task.id}. {task.title} [{status}] (Priority: {task.priority}, Due: {due})")
            
            save_tasks(tasks)
        
        elif choice == "3":
            task = get_valid_task_id(tasks, "mark as completed")
            if not task:
                continue

            if task.completed:
                print("Task is already completed.")
            else:
                task.completed = True
                print("Task marked as completed.")
            
            save_tasks(tasks)
        
        elif choice == "4":
            task = get_valid_task_id(tasks, "delete")
            if not task:
                continue

            tasks.remove(task)
            print("Task deleted successfully.")

            save_tasks(tasks)
                
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()