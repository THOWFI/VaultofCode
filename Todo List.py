def display_list(todo_list):
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")
def main():
    todo_list = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
