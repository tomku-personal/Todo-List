'''
ToDo List Text version

'''

todos = []

while True:
    action = input("What would you like to do? (add, edit, remove, show, quit): ").strip().lower()
    match action:
        case "add":
            todo = input("Enter a new todo: ").strip()
            if todo:
                todos.append(todo)
                print(f"Added todo: {todo}")
            else:
                print("Todo cannot be empty.")
        case "edit":
            index = int(input(f"Enter the index of the todo to edit (0 to {len(todos)-1}): "))
            if 0 <= index < len(todos):
                new_todo = input("Enter the new todo: ").strip()
                if new_todo:
                    todos[index] = new_todo
                    print(f"Updated todo at index {index} to: {new_todo}")
                else:
                    print("Todo cannot be empty.")
            else:
                print("Invalid index.")
        case "remove":
            index = int(input(f"Enter the index of the todo to remove (0 to {len(todos) - 1}): "))
            if 0 <= index < len(todos):
                removed_todo = todos.pop(index)
                print(f"Removed todo: {removed_todo}")
            else:
                print("Invalid index.")
        case "show":
            if todos:
                for i, todo in enumerate(todos):
                    print(f"{i}: {todo}")
            else:
                print("No todos available.")
        case "quit " | "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid action. Please try again.")

