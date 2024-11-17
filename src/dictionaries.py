# Creating a dictionary to store information about a person
class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"{self.name}'s phone number updated to {self.phone}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email updated to {self.email}")

def manualDict():
    print("manual dictionary") # aka Literal syntax
    #Best for static data: {} literal syntax, which is slightly 
    #more efficient and more readable for predefined dictionaries.
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "email": "alice@example.com"
    }

    # Accessing values using keys
    #print(person["name"])  # Output: Alice
    #print(person["city"])  # Output: New York

    # Adding a new key-value pair
    person["phone"] = "123-456-7890"

    # Modifying an existing key-value pair
    person["age"] = 31

    # Removing a key-value pair
    del person["email"]

    print(person)
    print("\n")

def funcDict():
    print("function dictionary") # aka dict() constructor, slower than {} because function call to dict()
    #Best for readability with nested data: dict(), 
    #particularly when creating nested dictionaries or using variables for keys/values.
    contacts = dict(
        Alice=dict(name="Alice", phone="123-456-7890", email="alice@example.com"),
        Bob=dict(name="Bob", phone="987-654-3210", email="bob@example.com")
    )

    # Accessing Bob's phone number
    print(contacts["Bob"]["phone"])  # Output: 987-654-3210

    # Adding a new contact
    contacts["Charlie"] = dict(phone="555-555-5555", email="charlie@example.com")

    # Modifying Alice's phone number
    contacts["Alice"]["phone"] = "111-222-3333"

    # Displaying the updated contacts
    print(contacts["Alice"])


def main(): 
    #manualDict()
    #funcDict()
    #print("\n")

    # Creating a contact book using a dictionary to store Person objects
    contacts = {
        "Alice": Person("Alice", "123-456-7890", "alice@example.com"),
        "Bob": Person("Bob", "987-654-3210", "bob@example.com")
    }

    # Accessing and using methods on a specific person
    contacts["Alice"].display_info()  # Output: Name: Alice, Phone: 123-456-7890, Email: alice@example.com
    contacts["Bob"].update_phone("111-222-3333")  # Updates Bob's phone number

    # Adding a new contact
    contacts["Charlie"] = Person("Charlie", "555-555-5555", "charlie@example.com")

    # Display all contacts
    for person in contacts.values():
        person.display_info()
    

if __name__ == "__main__":
    main()