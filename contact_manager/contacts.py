import os
import json
import csv
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


    def is_valid_number(self, number):
        return re.fullmatch(r'\+?\d{9,15}', number) is not None

    def add_new_contact(self, name, number):
        """Adds ne contact to file"""
        if not self.is_valid_number(number):
            print("Invalid phone number. It must be 9-15 digits and may start with +.")
            return
        
        if name.lower() in self.contacts:
            print(f"Contact with name {name} exists!")
        else:
            self.contacts[name.lower()] = number
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
        return self.contacts.get(name.lower(), "Contact not Found")


    def delete_contact(self,name):
        """Delete contact by name."""
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            self._save_contacts() #Auto save after deleting contact
            print(f"Contact {name} was deleted.")
        else:
            print(f"Contact {name} not found.")

    def export_to_csv(self, contacts, file_path = "contact_manager/data/contacts_export.csv"):
        """Exports all contacts to CSV file."""
        try:
            with open(file_path, mode= "w", newline= "") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "number"]) #Header
                for name, number in contacts.items():
                    writer.writerow([name, number])
                print(f"Contacts where successfully exported to {file_path}.")
        except Exception as e:
            print(f"Export to CSV was unsuccessfull : {e}")
