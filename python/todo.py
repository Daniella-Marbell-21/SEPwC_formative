import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
         file.write(task + "\n")
    
def list_tasks():
    if not os.path.exists(TASK_FILE):
        print("No tasks have been added yet.")
        return
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines()]
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for index, task in enumerate(tasks,1):
                    print(f"{index}. {task}")               
  

def remove_task(index):
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
