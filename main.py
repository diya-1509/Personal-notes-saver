note = input("Enter your notes: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

with open("notes.txt", "r") as file:
    notes = file.read()
    print(notes)

print("1. Add a note")
print("2. View all notes")
print("3. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    print("Add a note selected.")
elif choice == "2":
    print("View all notes selected.")
elif choice == "3":
    print("Exiting the program.")
else:
    print("Invalid choice. Please select either 1, 2, or 3.")

if choice == "1":
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")
elif choice == "2":
    with open("notes.txt", "r") as file:
        notes = file.read()
        print("Your notes:")
        print(notes)
