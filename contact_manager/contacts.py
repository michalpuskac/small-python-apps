import os
import json
import csv
import re
class ContactManager:
    def __init__(self, file_path = "contact_manager/data/contacts.json"):
        self.file_path = file_path
        self.contacts = self._load_contacts()


    def _load_contacts(self):
        """Read contacts from JSON file into dictionary with error hangdling."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    return json.load(file)
            else:
                # If file doesn't exist, initialize an empty contacts dictionary
                print(f"Info: Contacts file '{self.file_path}' not found. Starting with an empty contact list.")
                return {}

        except json.JSONDecodeError:
            print(f"Error: The contacts file '{self.file_path}' is corrupted and cannot be loaded. Starting with an empty contact list.")
            return {}
        except FileNotFoundError:
            print(f"Error: The specified file '{self.file_path}' could not be found.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}


    def _save_contacts(self):
        """Save contacts to JSON file."""
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok= True)
            with open(self.file_path, "w") as file:
                json.dump(self.contacts, file, indent=4)

        except FileNotFoundError:
            print(f"Error: The directory for '{self.file_path}' does not exist and could not be created.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def is_valid_number(self, number):
        return re.fullmatch(r'\+?\d{9,15}', number) is not None

    def add_new_contact(self, name, number):
        """Adds ne contact to file"""
        if not self.is_valid_number(number):
            print("Invalid phone number. It must be 9-15 digits and may start with +.\n")
            return
        if name.lower() in self.contacts:
            print(f"Contact with name {name} already exists!")
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
        return self.contacts.get(name.lower(), "Contact not Found\n")


    def delete_contact(self,name):
        """Delete contact by name."""
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            self._save_contacts() #Auto save after deleting contact
            print(f"Contact {name} was deleted.")
        else:
            print(f"Contact {name} not found.\n")

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
            print(f"Export to CSV was unsuccessfull : {e}\n")
