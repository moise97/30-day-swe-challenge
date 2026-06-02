# list and dictionary day 6 
contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts yet")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found")           



def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print(f"{name} not found")    


add_contact("Moise", "555-1234")
add_contact("Angel", "555-0000")
add_contact("Jordan", "555-9999")



print ("\nAll contacts:")
view_contacts()

print ("\nSearch for Moise:")
search_contact("Moise")

print ("\nSearch for someone not there:")
search_contact("Bob")

print ("\nDelete Angel:")
delete_contact("Angel")

print("\nContacts after delete:")
view_contacts()


def names_to_dict(names):
    result = {}
    for name in names:
        result[name] = len(name)
    return result 


print(names_to_dict(["Moise", "Angel", "Jordan"]))
