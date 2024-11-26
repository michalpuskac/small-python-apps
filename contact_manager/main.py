from contacts import ContactManager


def main():
    manager = ContactManager()
    4
    while True:
        print("\n---Contact Manager---")
        print("1.---Add new contact---")
        print("2.---Show all contacts---")
        print("3.---Search contact---")
        print("4.---Delete contact---")
        print("5.---Export all contacts to CSV---")
        print("---For exit type 'EXIT'---\n")

        choice = input("What you want to do. Choose 1, 2, 3, 4 or 5: ")
        
        if choice == "1":
            name = input("Enter name of contact: ").title()
            number = input("Enter name of contact: ")
            manager.add_new_contact(name, number)
            
        elif choice == "2":
            manager.show_all_contacts()

        elif choice == "3":
            name = input("Enter name of contact you want find: ").title()
            print(manager.search_contact(name))

        elif choice == "4":
            name = input("Enter name of contact you want to delete: ").title()
            manager.delete_contact(name)


        elif choice == "5":
            manager.export_to_csv(manager.contacts)

        elif choice.lower() == "exit":
            print("Program terminated.")
            break
        else:
            print("\nInvalid input. Try again with choice 1 to 5 or 'exit'")
        

if __name__ == "__main__":
    main()