
def todo_list_app():
    tasks = []

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"✅ Task added: {task}")

        elif choice == "2":
            if not tasks:
                print("📭 No tasks yet!")
            else:
                print("📋 Your tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("❌ Nothing to remove!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                remove_index = int(input("Enter the number of the task to remove: "))
                if 1 <= remove_index <= len(tasks):
                    removed = tasks.pop(remove_index - 1)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("⚠️ Invalid task number.")

        elif choice == "4":
            print("👋 Goodbye! Your tasks won't be saved this time.")
            break

        else:
            print("❗ Invalid option, please try again.")

todo_list_app()
