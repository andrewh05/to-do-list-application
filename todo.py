tasks = []


def show_menu():
  print("\nto do list menu")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. View Tasks")
  print("4. Exit")


def add_task():
  task = input("Enter the task: ")
  tasks.append(task)
  print("Task added successfully!")


def remove_task():
  view_tasks()
  try:
    task_index = int(input("Enter the task number to remove: ")) -1
    if 0 <= task_index < len(tasks):
      removed_task = tasks.pop(task_index)
      print(f"Task '{removed_task}' removed.")
    else:
      print("invalid task number")
  except ValueError:
    print("Invalid input. Please enter a number.")


def view_tasks():
  if tasks:
    print("\nyour tasks")
    for index, task in enumerate(tasks, start=1):
      print(f"{index}. {task}")
  else:
    print("No tasks found.")


def main():
  while True:
    show_menu()
    choice = input("Choose an option between (1 - 4) ")
    if choice == "1":
      add_task()
    elif choice == "2":
      remove_task()
    elif choice == "3":
      view_tasks()
    elif choice == "4":
      print("Exiting the program")
      break


if __name__ == "__main__":
  main()
