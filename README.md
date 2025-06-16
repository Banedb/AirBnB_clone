# 0x00. AirBnB clone - The console
This project aims to develop a command-line interface (CLI) for managing data within an Airbnb-like application. The CLI allows users to perform various operations such as creating, updating, deleting, and displaying instances of different classes within the application, such as users, places, reviews, etc.

## Command Interpreter
The command interpreter is a Python-based CLI tool that provides a command-line interface for interacting with the Airbnb application. It allows users to execute commands to perform CRUD (Create, Read, Update, Delete) operations on different resources within the application.

### How to Start the Command Interpreter
- To start the command interpreter, follow these steps:

- Clone the project repository to your local machine.

- Navigate to the directory containing the project files.

- Run the console.py file with: "./console.py" or "python console.py"

- Type "help" in the console for documentation.

### Available Commands
The command interpreter supports the following commands:

- "all": Display all instances or all instances of a specified class.
- "count": Count instances of a specified class.
- "create": Create a new instance of a specified class.
- "destroy": Delete a specified instance.
- "help": Display a list of available commands or provide help for a specific command.
- "show": Display details of a specific instance.
- "quit" | "exit" | "EOF": Exit the console.
- "update": Update attributes of a specified instance.

`Enter` on an empty line does nothing.

### Supported Classes
The command interpreter supports CRUD operations on the following classes:

- "BaseModel": The base class for all other classes. Provides basic functionality such as serialization and deserialization.
- "User": Represents a user of the application.
- "Place": Represents a lodging place available for booking.
- "Review": Represents a review written by a user for a place.
- "City", "State", "Amenity": Additional classes representing geographical and other data related to places.

### Testing
The project includes unit tests to ensure the correctness of the implemented functionality. To run the tests, execute the following commands:
- "python3 -m unittest discover tests"
- "echo 'python3 -m unittest discover tests' | bash" (In non-interactive mode)
