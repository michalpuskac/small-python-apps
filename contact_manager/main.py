from contacts import Contact, ContactManager


def main():
    manager = ContactManager()
    4
    while True:
        print("\n---Contact Manager---")
        print("1.---Add new contact---")
        print("2.---Show all contacts---")
        print("3.---Search contact---")
        print("4.---End of program---\n")

        choice = input("What you want to do. Choose 1, 2, 3 or 4: ")
        
        if choice == "1":
            name = input("Enter name of contact: ")
            while name == "":
                name = input("Enter name of contact: ")
            number = input("Enter phone number: ")
            while number == "":
                number = input("Enter name of contact: ")
            new_contact = Contact(name, number)
            manager.add_new_contact(new_contact)
            

        elif choice == "2":
            manager.show_all_contacts()
        elif choice == "3":
            name = input("Enter name of contact you want find: ")
            result = manager.search_contact(name)
            print(result)
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("\nInvalid input. Try again with choice 1, 2, 3 or 4")
        

if __name__ == "__main__":
    main()