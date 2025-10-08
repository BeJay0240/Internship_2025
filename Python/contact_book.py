import csv

CONTACTS_FILE = 'contacts.csv'
HEADERS = ['Name', 'Phone', 'Email']

def load_contacts():
    """Loads contacts from the CSV file."""
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        # If the file doesn't exist, it will be created when saving
        pass
    return contacts

def save_contacts(contacts):
    """Saves contacts to the CSV file."""
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    """Adds a new contact to the contact list."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")

    new_contact = {'Name': name, 'Phone': phone, 'Email': email}
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    """Displays all contacts in the contact list."""
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Your Contacts ---")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    print("---------------------\n")

def delete_contact(contacts):
    """Deletes a contact from the contact list."""
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index_to_delete = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index_to_delete < len(contacts):
            deleted_contact = contacts.pop(index_to_delete)
            save_contacts(contacts)
            print(f"Contact '{deleted_contact['Name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()