from contacts import ContactManager

def menu():
    print("\n---Contact Manager---")
    print("1.---Add new contact---")
    print("2.---Show all contacts---")
    print("3.---Search contact---")
    print("4.---Delete contact---")
    print("5.---Export all contacts to CSV---")
    print("---For exit type 'EXIT'---\n")

def main():
    manager = ContactManager()

    menu()
    while True:
        choice = input("**What you want to do. Choose 1, 2, 3, 4 or 5**: ")
        if choice not in {"1", "2", "3", "4", "5", "exit"}:
            print("Invalid input. Try again with choice 1 to 5 or 'exit'\n")
            continue
        
        if choice == "1":
            name = input("Enter name of contact: ").strip()
            number = input("Enter name of contact: ").strip()
            manager.add_new_contact(name, number)

        elif choice == "2":
            manager.show_all_contacts()
            menu()

        elif choice == "3":
            name = input("Enter name of contact you want find: ").strip()
            print(manager.search_contact(name))

        elif choice == "4":
            name = input("Enter name of contact you want to delete: ").strip()
            manager.delete_contact(name)


        elif choice == "5":
            manager.export_to_csv(manager.contacts)

        elif choice.lower() == "exit":
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()