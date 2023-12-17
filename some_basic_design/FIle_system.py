"""
Store some data in File system.
"""

"""
NOTE:

1. dependency-free: Since static methods do not have access to instance-specific data, they can be written without dependencies on other instance methods or variables. This can lead to decoupled code and improved maintainability.
2. Code Reusability: Static methods can be reused across multiple instances or classes without duplication. They provide a centralized location for common functionality that can be shared by different parts of the codebase.
3. Limited Access: Static methods cannot access or modify instance-specific data or methods. They operate solely on their input parameters and any other static data within the class. This can limit their usefulness in certain scenarios where access to instance data is necessary.

4. Inflexibility: Static methods cannot be overridden by subclasses. This means that if a static method is defined in a base class, it will always be the same in all derived classes. This can restrict the flexibility and extensibility of the code.
"""
import json

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return User(data['name'], data['email'])

# Create a list of user objects
users = [
    User("John Doe", "john@example.com"),
    User("Jane Smith", "jane@example.com"),
    User("Alice Brown", "alice@example.com"),
    User("Bob Johnson", "bob@example.com"),
    User("Eve Wilson", "eve@example.com")
]

# Store user objects in a file
file_path = 'users.json'

with open(file_path, 'w') as file:
    serialized_users = [user.to_dict() for user in users]
    json.dump(serialized_users, file)

# Retrieve and display user objects from the file
with open(file_path, 'r') as file:
    serialized_users = json.load(file)
    retrieved_users = [User.from_dict(data) for data in serialized_users]

# Display the retrieved user objects
for user in retrieved_users:
    print(f"Name: {user.name}, Email: {user.email}")


# Another eg.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return User(data['name'], data['email'])

# Creating a User object from a dictionary
user_data = {'name': 'John Doe', 'email': 'john@example.com'}
user = User.from_dict(user_data)



import unittest

class UserTest(unittest.TestCase):
    def test_to_dict(self):
        # Create a User object
        user = User("John Doe", "john@example.com")

        # Call the to_dict() method
        user_dict = user.to_dict()

        # Assert that the returned dictionary has the correct keys and values
        self.assertEqual(user_dict['name'], "John Doe")
        self.assertEqual(user_dict['email'], "john@example.com")

    def test_from_dict(self):
        # Create a dictionary representing user data
        user_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com'
        }

        # Call the from_dict() method
        user = User.from_dict(user_data)

        # Assert that the created User object has the correct attributes
        self.assertEqual(user.name, "Jane Smith")
        self.assertEqual(user.email, "jane@example.com")

if __name__ == '__main__':
    unittest.main()
