import os
import json
import csv
import re
from pathlib import Path
from tabulate import tabulate
from shutil import copy2
class ContactManager:
    def __init__(self, file_path = None):
        """Define defaul path: a hidden folder  in the user's home directory"""
        default_dir = Path.home() / "ContactManager"
        default_path = default_dir / "contacts.json"

        self.file_path = Path(file_path) if file_path else default_path
        #Ensure defaul directory exists if using the default path
        if not file_path:
            default_dir.mkdir(parents=True, exist_ok= True)
        
        self.contacts = self._load_contacts()


    def _load_contacts(self):
        """Read contacts from JSON file into dictionary with error hangdling."""
        try:
            if self.file_path.exists():
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
            if self.file_path.exists():
                backup_path = self.file_path.with_suffix(".bak")
                copy2(self.file_path, backup_path)
                print(f"Backup created: {backup_path}")
                
            with open(self.file_path, "w") as file:
                json.dump(self.contacts, file, indent=4)

        except FileNotFoundError:
            print(f"Error: The directory for '{self.file_path}' does not exist and could not be created.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def is_valid_number(self, number):
        return re.fullmatch(r'\+?\d{9,15}', number) is not None


    def add_new_contact(self, name, number):
        """Adds new contact to file"""
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
            print(tabulate(self.contacts.items(), headers = ["Name", "Phone number"], tablefmt ="grid"))
            # print("\n--Contact list--")
            # for name, number in self.contacts.items():
                # print(f"Name: {name}, Phone number: {number}")


    def search_contact(self, name):
        """Search contact by name"""
        result = self.contacts.get(name.lower())
        if result:
            table = [["Name", "Phone number"], [name.title(), result]]
            return tabulate(table, headers="firstrow", tablefmt="grid")
        else:
            return "Contact not Found\n"


    def delete_contact(self,name):
        """Delete contact by name."""
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            self._save_contacts() #Auto save after deleting contact
            print(f"Contact {name} was deleted.")
        else:
            print(f"Contact {name} not found.\n")


    def export_to_csv(self, contacts, file_path = None):
        """Exports all contacts to CSV file."""
        file_path = file_path or self.file_path.with_suffix(".csv")
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, "w", newline= "") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone number"]) #Header
                for name, number in self.contacts.items():
                    writer.writerow([name.title(), number])
                print(f"Contacts successfully exported to {file_path}.")
        except Exception as e:
            print(f"Export to CSV was unsuccessfull : {e}\n")
