# Contact Manager

## Overview

The Contact Manager is a Python-based application designed to manage personal or professional contacts . It alows users to perform various actions such as adding, searching, deleting, and exporting contacts to a CSV file. The program ensures data integrity and provides interface via the command line.

The application is modular, with separate components for functionality (contacts.py), interaction (main.py), and testing (test_contact_manager.py). It adheres to Pythonic principles and is tested to ensure reliability.

## Features

 - Add Contacts: Save names and phone numbers.
 - Search Contacts: Find contacts by name with case-insensitive matching.
 - Delete Contacts: Remove unwanted entries.
 - Export Contacts: Save all contacts to a CSV file.
 - Robust Error Handling: Ensures smooth user experience.
 - Backup: Automatically creates a backup of contact data before overwriting.
 - Testing: Includes comprehensive unit tests using pytest.

## Why Modular Design?

This project follows a modular design to ensure maintainability and scalability:

1. contacts.py:
 - Contains the core ContactManager class with all business logic.
 - Encapsulates data handling and ensures separation of concerns.
2. main.py:
 - Handles user interaction through a command-line interface.
 - Keeps the logic separate from the core functionality.
3. test_contact_manager.py:
 - Ensures correctness and reliability using automated tests.

Modular design also simplifies debugging, testing, and extending the application.

## Setup Instructions

**1. Clone the Repository**

        git clone <repository-url>
        cd contact_manager

**2. Create a Virtual Environment**

It is recommended to use a virtual environment to manage dependencies.

        python3 -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate

**3. Install Dependencies**

Install the required Python packages from the requirements.txt file:

        pip install -r requirements.txt

### Dependencies

 - Python 3.13+
 - Packages (see requirements.txt):
 - pytest: For testing.
 - tabulate: For formatted output.
 - colorama: For terminal color support (Windows).
 - packaging, pluggy, iniconfig: Dependencies for pytest.

## How to Run the Application

Run the main script to interact with the Contact Manager:

python main.py

### Example Interaction

        --- Contact Manager ---
        1. Add new contact
        2. Show all contacts
        3. Search contact
        4. Delete contact
        5. Export all contacts to CSV
        Type 'exit' to quit

## How to Run Tests

The application includes comprehensive tests using pytest. To run the tests:

pytest test_contact_manager.py

This will validate the functionality of all core features, ensuring the application works as expected.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this application as per the terms of the license.