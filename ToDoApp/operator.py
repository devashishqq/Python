from Classes import Todo

user_name = input("Enter your name: ")
user_name = Todo(user_name)

while True:
    choice = input("1: Add  2: Remove  3: Exit → ")

    if choice == "1":
        sno = input("Serial number: ")
        note = input("Task: ")
        time = input("Time: ")
        user_name.create(sno, note, time)

    elif choice == "2":
        sno = input("Serial number to delete: ")
        user_name.delete(sno)

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice.")

user_name.showtodo()