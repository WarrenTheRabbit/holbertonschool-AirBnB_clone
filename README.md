## Description

This collaborative project forms an integral component of the Holberton School Full-Stack Software Engineer curriculum, representing the outset of crafting an AirBnB replica. Within this project phase, we construct a tailored command-line interface for effective data administration while simultaneously laying the foundation for data storage through the establishment of fundamental classes. Users, through the utilization of console commands, have the capability to generate, modify, and delete objects, along with overseeing file storage. The system utilizes JSON serialization/deserialization to ensure enduring storage across sessions.

## Compilation/Installation
To compile and install the AirBnB Clone Command Interpreter, follow these steps:

1. Clone the repository from GitHub:
```
git clone <repository_url>
```

3. Once cloned, navigate to the directory containing the "console.py" file. Run the command interpreter using the following command:
```
/AirBnB_clone$ ./console.py
```
After executing this command, you should see the following prompt:
```
(hbnb)
```
This prompt indicates that you are now in the "HBnB" console.

## How to use the application

Within this console, you have access to a variety of commands:

- create: Creates an instance based on a given class.
- destroy: Deletes an object based on its class and UUID.
- show: Displays details of an object based on its class and UUID.
- all: Displays all objects the program has access to, or all objects of a given class.
- update: Modifies existing attributes of an object based on its class name and UUID.
- quit: Exits the program (EOF will do the same).

## Examples

Example 0: Create an object
```
(hbnb) create BaseModel
```

Example 1: Show an object
```
(hbnb) show BaseModel ff241d82-f44d-4a24-883e-0e4851fca803
[BaseModel] (ff241d82-f44d-4a24-883e-0e4851fca803) {'id': 'ff241d82-f44d-4a24-883e-0e4851fca803', 'created_at': datetime.datetime(2024, 3, 2, 15, 16, 53, 845381), 'updated_at': datetime.datetime(2024, 3, 2, 15, 16, 53, 845396)}
(hbnb)
```

Example 2: Destroy an object
```
(hbnb) destroy BaseModel ff241d82-f44d-4a24-883e-0e4851fca803
```

Example 3: Update an object
```
(hbnb) update BaseModel ff241d82-f44d-4a24-883e-0e4851fca803 first_name "Daniel"
(hbnb) show BaseModel ff241d82-f44d-4a24-883e-0e4851fca803
[BaseModel] (ff241d82-f44d-4a24-883e-0e4851fca803) {'id': 'ff241d82-f44d-4a24-883e-0e4851fca803', 'created_at': datetime.datetime(2024, 3, 2, 15, 16, 53, 845381), 'updated_at': datetime.datetime(2024, 3, 2, 15, 18, 16, 335696), 'first_name': 'Daniel'}
```

Example 4: Show all objects
```
(hbnb) all
["[BaseModel] (ff241d82-f44d-4a24-883e-0e4851fca803) {'id': 'ff241d82-f44d-4a24-883e-0e4851fca803', 'created_at': datetime.datetime(2024, 3, 2, 15, 16, 53, 845381), 'updated_at': datetime.datetime(2024, 3, 2, 15, 18, 16, 335696), 'first_name': 'Daniel'}", "[BaseModel] (34b334f4-2a12-4226-95be-0795eac6e618) {'id': '34b334f4-2a12-4226-95be-0795eac6e618', 'created_at': datetime.datetime(2024, 3, 2, 15, 19, 47, 404121), 'updated_at': datetime.datetime(2024, 3, 2, 15, 19, 47, 404133)}", "[User] (be763bed-fccb-44e2-b614-036e82f61b0b) {'id': 'be763bed-fccb-44e2-b614-036e82f61b0b', 'created_at': datetime.datetime(2024, 3, 2, 15, 19, 59, 330078), 'updated_at': datetime.datetime(2024, 3, 2, 15, 19, 59, 330090)}"]
```
