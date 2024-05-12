import json
import os
from datetime import datetime, timedelta

# File paths for storing contacts and notes
CONTACTS_FILE = "contacts.json"


# Initialize contacts and notes dictionaries
contacts = {}


# Load existing data from files (if any)
if os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "r") as f:
        contacts = json.load(f)


# Function to save contacts and notes to files
def save_data():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# Function to add a new contact
def add_contact(name, address, phone, email, birthday):
    contact_id = len(contacts) + 1
    contacts[contact_id] = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "birthday": birthday
    }
    save_data()
    print("Contact added successfully.")

# Function to list all contacts
def list_contacts():
    if contacts:
        for contact_id, contact in contacts.items():
            print(f"{contact_id}: {contact['name']}")
    else:
        print("No contacts found.")

# Function to search for contacts by name
def search_contacts_by_name(name):
    found = False
    for contact_id, contact in contacts.items():
        if name.lower() in contact['name'].lower():
            print(f"{contact_id}: {contact['name']}")
            found = True
    if not found:
        print("No matching contacts found.")

# Function to delete a contact
def delete_contact(contact_id):
    if contact_id in contacts:
        del contacts[contact_id]
        save_data()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Function to display upcoming birthdays
def upcoming_birthdays(days):
    upcoming_date = datetime.now() + timedelta(days=days)
    upcoming_contacts = [
        contact for contact in contacts.values()
        if contact['birthday'] and datetime.strptime(contact['birthday'], "%Y-%m-%d").date() <= upcoming_date.date()
    ]
    if upcoming_contacts:
        print("Upcoming birthdays:")
        for contact in upcoming_contacts:
            print(f"{contact['name']}: {contact['birthday']}")
    else:
        print("No upcoming birthdays.")

# Main function to handle user input
def main():
    while True:
        print("\nPersonal Assistant CLI")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contacts by Name")
        print("4. Delete Contact")
        print("5. Upcoming Birthdays")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (YYYY-MM-DD): ")
            add_contact(name, address, phone, email, birthday)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contacts_by_name(name)
        elif choice == "4":
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == "5":
            days = int(input("Enter number of days for upcoming birthdays: "))
            upcoming_birthdays(days)
        elif choice == "6":
            print("Exiting Personal Assistant. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()