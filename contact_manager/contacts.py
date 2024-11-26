import os 
import re

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def format_contact(self):
        """Returns a contact as a string"""
        return f"{self.name}, {self.number}\n"


class ContactManager:
    def __init__(self, file_path = "contact_manager/data/contacts.csv"):
        self.file_path = file_path

        #Check if the folder (data) exists. If does not, create it.
        folder_path = os.path.dirname(self.file_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)

        # Check if file (contacts) exists. If does not, create it.
        if not os.path.exists(self.file_path):
            with open(self.file_path, "a") as file:
                file.write("name,number\n")


    def add_new_contact(self, contact):
        """Adds ne contact to file"""
        with open(self.file_path, "a") as file:
            file.write(contact.format_contact())


    def show_all_contacts(self):
        """Print all saved contact in file"""
        try:
            with open("contact_manager/data/contacts.csv", "r") as file:
                print("All Contacts:")
                for line in file.readlines()[1:]: #skip header of list/dict
                    name, number = line.strip().split(",")
                    print(f"Name: {name}, Phone number: {number}")
        except FileNotFoundError:
            print("\nContact file does not exist")


    def search_contact(self,name):
        """Search contact by name"""
        try:
            with open(self.file_path, "r") as file:
                for line in file.readlines()[1:]:
                    contact_name, number = line.strip().split(",")
                    if contact_name.lower() == name.lower():
                        return  f"Name: {contact_name}, Phone number: {number}"
            return "\nContact was not found"
        except FileNotFoundError:
            print("\nContact file does not exist")
    