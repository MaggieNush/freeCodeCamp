def add_contact(contacts, contact_tuple):
    name = contact_tuple[0].lower()
    phone_number = contact_tuple[1]

    if name in contacts:
        return f"Contact '{name}' already exists"
    else:
        contacts[name] = phone_number
        return f"Contact '{name}' added with phone_number {phone_number}"
    
        
    
def update_contact(contacts, contact_tuple):
    name = contact_tuple[0].lower()
    phone_number = contact_tuple[1]

    if name in contacts:
        contacts[name] = phone_number
        return f"{phone_number} updated successfully!"
    
    else:
        return f"'{name}' does not exist!"
    
def delete_contact(contacts, name):
    name = name.lower()

    if name in contacts:
        del contacts[name]
        return f"'{name}' deleted successfully!"
    else:
        return f"'{name}' does not exist!"
    
def find_contact(contacts, name):
    name = name.lower()
    

    if name in contacts:
        """Get phone number from contacts dictionary"""
        phone_number = contacts[name] 
        return f"{name}: {phone_number}"
    else:
        return f"Contact '{name}' not found."
    
def view_all_contacts(contacts):
    if not contacts:
        return "No names in contacts"
    
    result = "Current Contacts: "

    for name, phone_number in contacts.items():
        result += f"{name.capitalize()}: {phone_number}\n"
    return result

test_code = {}
print(add_contact(test_code, ("Maria", 712345678)))
print(add_contact(test_code, ("Amboko", 702345678)))
print(add_contact(test_code, ("Wainaina", 787654321)))
print(update_contact(test_code, ("Wendi", 712345687)))
print(view_all_contacts(test_code))