'''
A table-driven todo list. 
This version uses a command processor table to handle user commands.
It allows for easier expansion and modification of the command handling logic.
'''

from dataclasses import dataclass
from typing import Callable

@dataclass
class CommandProcessor:
    command: str
    processor: Callable[..., None]

todos = list()

# defining the command processor functions
def add_todo():
    todo = input("Enter a new todo item: ")
    todos.append(todo)
    print(f"Added todo: {todo}")

def list_todos():
    if todos:
        print("Todo list items:")
        for i, todo in enumerate(todos):
            print(f"{i+1}-{todo}")  # enumerate starts from 1 for user-friendliness
    else:
        print("Todo list is empty.")

def remove_todo():
    if not todos:
        print("Todo list is empty.")
        return
    list_todos()
    index = int(input("Enter the number of the todo item to remove: ")) - 1
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"Removed todo: {removed}")
    else:
        print("Invalid index.")

def clear_todos():
    todos.clear()

    print("Cleared all todos.")

def edit_todo():
    if not todos:
        print("Todo list is empty.")
        return
    list_todos()
    index = int(input("Enter the number of the todo item to edit: ")) - 1
    if 0 <= index < len(todos):
        new_todo = input("Enter the new todo item: ")
        todos[index] = new_todo
        print(f"Updated todo: {new_todo}")
    else:
        print("Invalid index.")

def remove_todo():
    if not todos:
        print("Todo list is empty.")
        return
    list_todos()
    index = int(input("Enter the item of the todo item to remove: ")) - 1
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"Removed todo: {removed}")
    else:
        print("Invalid index.")

def quit_todo():
    print("Exiting the todo list. Goodbye!")
    global exit  # access the global exit variable
    exit = True  # signal to exit the loop

# The table of command processors
command_processors = [
    CommandProcessor("add", add_todo),
    CommandProcessor("list", list_todos),
    CommandProcessor("show", list_todos),  # alias for list
    CommandProcessor("remove", remove_todo),
    CommandProcessor("clear", clear_todos),
    CommandProcessor("edit", edit_todo),
    CommandProcessor("quit", quit_todo),
    CommandProcessor("exit", quit_todo)]  # alias for quit
commands = [cp.command for cp in command_processors]

exit = False  # control variable for the main loop

while not exit:
    command = input(f"Enter command ({', '.join(commands)}): ").strip().lower()
    if command in commands:
        for cp in command_processors:
            if cp.command == command:
                cp.processor()  # call the corresponding processor function
    else:
        print("Invalid command. Please try again.")








