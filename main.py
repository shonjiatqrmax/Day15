import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks_15.txt")

def save_tasks():
    with open(FILE_NAME,"w") as file:
        for task in tasks:
            file.write(task["task"]+","+task["priority"]+"\n")

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) == 2:
                    task, priority = parts
                else:
                    # 旧数据，没有priority
                    task = parts[0]
                    priority = "Low"

                tasks.append({
                    "task": task,
                    "priority": priority
                })
    except FileNotFoundError:
        print("No existing file, starting fresh.")
    
    return tasks

def update_task():
    if len(tasks) == 0:
        print("No tasks to update.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 99))

    for i, t in enumerate(sorted_tasks):

        print(f"{i}. {t['task']} - {t['priority']}")

    index = int(input("Enter index to update: "))

    if 0 <= index < len(sorted_tasks):
        task_to_update = sorted_tasks[index]

        new_task = input("Enter new task (leave blank to keep same): ")
        new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()

        # 更新 task 内容
        if new_task:
            task_to_update["task"] = new_task

        # 更新 priority
        if new_priority in ["High", "Medium", "Low"]:
            task_to_update["priority"] = new_priority

        save_tasks()
        print("✔ Task updated!")
    else:
        print("❌ Invalid index")


priority_order={
     "High":1,
     "Medium":2,
     "Low":3
}

tasks=load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        priority=input("Enter priority(High/Medium/Low):").capitalize()

        if priority not in ["High","Medium","Low"]:
                            print("Invalid priority, set to low")
                            priority="Low"
                            
        tasks.append({
             "task":task,
             "priority": priority
             })
        save_tasks()
        print("✔ Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\n--- Your Tasks ---")
            # Sort tasks by priority
            sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 99))
            for i, task in enumerate(sorted_tasks):
                print(f"{i}. {task['task']} - {task['priority']}")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 99))

            for i, task in enumerate(sorted_tasks):
                print(f"{i}. {task['task']} - {task['priority']}")

            index = int(input("Enter index to delete: "))

            if 0 <= index < len(sorted_tasks):
                tasks_to_delete=sorted_tasks[index]
                tasks.remove(tasks_to_delete)
                save_tasks()
                print("✔ Task deleted!")
            else:
                print("❌ Invalid index")

    elif choice == "4":
        update_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice")