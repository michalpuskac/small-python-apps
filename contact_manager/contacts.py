import os
import json
import re
class ContactManager:
    def __init__(self, file_path = "contact_manager/data/contacts.json"):
        self.file_path = file_path
        self.contacts = self._load_contacts()


    def _load_contacts(self):
        """Read contacts from JSON file to dictionary."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {} #empty dictionary if JSON file does not exist


    def _save_contacts(self):
        """Save contacts to JSON file."""
        os.makedirs(os.path.dirname(self.file_path), exist_ok= True)
        with open(self.file_path, "w") as file:
            json.dump(self.contacts, file, indent=4)


    def add_new_contact(self, name, number):
        """Adds ne contact to file"""
        if name in self.contacts:
            print(f"Contact with name {name} exists!")
        else:
            self.contacts[name] = number
            self._save_contacts() #automatic save
            print(f"Contact {name} added.")


    def show_all_contacts(self):
        """Print all saved contact in file."""
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\n--Contact list--")
            for name, number in self.contacts.items():
                print(f"Name: {name}, Phone number: {number}")


    def search_contact(self, name):
        """Search contact by name"""
        return self.contacts.get(name, "Contact not Found")


    def delete_contact(self,name):
        """Delete contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            self._save_contacts() #Auto save after deleting contact
            print(f"Contact {name} was deleted.")
        else:
            print(f"Contact {name} not found.")