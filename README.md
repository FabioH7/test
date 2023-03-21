# AirBnB Clone

This project is an implementation of a command-line interface for an Airbnb clone application. The application allows users to create, update and delete objects in a simulated Airbnb database.

## Command Interpreter (Console Function)

The command interpreter is a CLI that allows users to interact with the Airbnb clone application. It provides a command-line interface for users to enter commands, which are then processed and executed by the interpreter. The interpreter reads user input, processes it, and displays the appropriate output.

## How to Start the Command Interpreter

To start the command interpreter, clone the repository and navigate to the project directory. Then, run the command:
```
$ ./console.py
```
This will start the command interpreter and display a prompt indicating that it is ready to receive user input.

## How to Use the Command Interpreter

To use the command interpreter, enter commands at the prompt and press enter. The interpreter will then process the command and display the appropriate output.

The available commands include:

- `create` - create a new object
- `show` - display information about an object
- `destroy` - delete an object
- `all` - display information about all objects
- `update` - update an object's information

For a full list of commands and their usage, enter the command `help` at the prompt.

## Examples

Here are some examples of how to use the command interpreter:
```
$ ./console.py
(hbnb) create User
7d257547-0516-47f6-820f-95b44d05b9ea
(hbnb) show User 7d257547-0516-47f6-820f-95b44d05b9ea
[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0)}
(hbnb) update User 7d257547-0516-47f6-820f-95b44d05b9ea name "John Doe"
(hbnb) show User 7d257547-0516-47f6-820f-95b44d05b9ea
[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'name': 'John Doe'}
(hbnb) all User
[[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10,
```
# Serialization and Deserialization
* ` Serialization is the process of converting an object into a stream of bytes that can be stored in a file or sent over a network. Deserialization is the process of converting the stream of bytes back into an object.`

* In this project, we use JSON as the serialization format. The object is first converted to a dictionary using the to_dict method, which is then converted to a JSON string using the json.dumps method. To deserialize, we first parse the JSON string using the json.loads method, which gives us a dictionary. We then create a new object using the create method and pass the dictionary as the object's attributes. (A network). Deserialization is the process of converting the stream of bytes back into an object.

# Package Imports Explained
* The project follows a modular approach to organizing the code. The project is divided into multiple packages, with each package containing modules that are responsible for a specific part of the application.

* To import a module from another package, we use the dot notation. For example, to import the BaseModel class from the models package, we use the following import statement:

```
from models.base_model import BaseModel
```
# Storage
The File Storage Layer provides an interface for storing and retrieving data from a file. The interface is defined in the FileStorage class, which provides the following methods:

* ```all(self):``` returns a dictionary of all objects in the storage
* ```new(self, obj):``` adds a new object to the storage
* ```save(self):``` saves the objects in the storage to a file
* ```reload(self):``` loads the objects from the file into the storage

# Program Flow
The main program flow of the application is as follows:

```
1.  The user starts the application by running console.py.
2.  The console.py script initializes the application by creating an instance of the HBNBCommand class and calling its cmdloop() method.
3.  The cmdloop() method displays a prompt and waits for user input.
4.  The user enters a command, which is processed by the HBNBCommand instance.
5.  The HBNBCommand instance passes the command to the appropriate layer for processing.
6.  The appropriate layer processes the command and returns the appropriate output.
7.  The output is displayed to the user.
8.  Steps 3-7 are repeated until the user exits using the quit function.
```
# Authors
The project was developed by a team of developers(Fabio), with each developer responsible for a specific part of the project(Shokt e Fabios). The distribution of work was as follows:
```
* Models Layer: Developed by Fabio
* File Storage Layer: Developed by Ennio
* Command Interpreter Layer: Developed by Patrik
```
