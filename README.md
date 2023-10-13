# AirBnB clone

Complete web app from front end to back end. It includes a console, a storage engine, a RESTful API and a front end with static and dynamic components.

## Console

### Description
We are building a command interpreter to manage objects. All other parts of the project will use this as a base, so it's an essential component of it.

### How we built it:
* First, we built a parent class called BaseModel. 
* We create a flow to serialize and deserialize, Instance <-> Dictionary <-> JSON string <-> file. 
* Classes for the project that inherit from BaseModel.
* First abstracted storage engine of the project: File storage.
* Create unittests to validate all classes and storage engine.

### How to use it?

Interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

Non-interactive mode: (like the Shell project in C)

$ echo help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
