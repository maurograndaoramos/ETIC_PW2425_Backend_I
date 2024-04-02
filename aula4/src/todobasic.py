todo_list = []

def add_entry():
    entry = input("Enter a new To-Do item: ")
    todo_list.append(entry)
    print("Item added.")

def remove_entry():
    if not todo_list:
        print("The To-Do list is empty.")
        return
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")
    try:
        choice = int(input("Enter the item number to remove: ")) - 1
        if 0 <= choice < len(todo_list):
            removed_item = todo_list.pop(choice)
            print(f"Removed item: {removed_item}")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def view_list():
    if not todo_list:
        print("The To-Do list is empty.")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def export_list():
    with open('todo_list.txt', 'w') as file:
        for item in todo_list:
            file.write(f"{item}\n")
    print("To-Do list exported to todo_list.txt.")

def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Export List")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            remove_entry()
        elif choice == '3':
            view_list()
        elif choice == '4':
            export_list()
        elif choice == '5':
            print("Exiting the To-Do List App.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
