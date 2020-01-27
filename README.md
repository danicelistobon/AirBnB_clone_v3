# :triangular_flag_on_post: Holberton B&B

<img align="center" src="https://i.ibb.co/d5N85Nh/hbnb.png" width="100%">

### Welcome to the AirBnB clone project! (Holberton B&B)

First step: write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

### Whats a command interpreter?

Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object

### HBNBCommand

This is the console (command interpreter) for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

Supported classes:
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

<img align="center" src="https://i.ibb.co/g6XHQFf/Diagrama.jpg" width="100%">

### Installation
* Clone this repository: `git clone https://github.com/danicelistobon/AirBnB_clone_v3.git`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

### Commands

These are some of the commands implemented in our console (HBNBCommand):

| Command | Description |
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name |
| create | Creates a new instance of class name, saves it (to the JSON file) and prints the id |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file) |
| help | List available commands with "help" or detailed help with "help cmd" |
| quit - EOF | Commands to exit the program |
| show | Prints the string representation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |

To start, navigate to the project folder and enter `./console.py` in the shell.

| Examples of how to use the commands |
| ------ |
| Create: |
| `create <class name>` Ex: `create BaseModel` |
| Show: |
| `show <class name> <object id>` Ex: `show User my_id` |
| Destroy: |
| `destroy <class name> <object id>` Ex: `destroy Place my_place_id` |
| All: |
| `all` or `all <class name>` Ex: `all` or `all State` |
| Quit: |
| `quit` or `EOF (Ctrl-d)` |
| Help: |
| `help` or `help <command>` Ex: `help` or `help all` |
| Additionally, the console supports: |
| `<class name>.<command>(<parameters>)` syntax. Ex: `City.show(my_city_id)` |

<img align="center" src="https://i.ibb.co/L5wPt65/Consola.jpg" width="60%">

### Environment variables

- HBNB_ENV: running environment. It can be dev or test for the moment (production soon!)
- HBNB_MYSQL_USER: the username of your MySQL
- HBNB_MYSQL_PWD: the password of your MySQL
- HBNB_MYSQL_HOST: the hostname of your MySQL
- HBNB_MYSQL_DB: the database name of your MySQL
- HBNB_TYPE_STORAGE: the type of storage used. It can be file (using FileStorage) or db (using DBStorage)

## Example

Example using the "console.py" file:

```
$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

## Authors

### AirBnB clone v1

Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)

Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)

### AirBnB clone v2

Joann Vuong

### AirBnB clone v3

Liliana Ospina Murillo - [Github](https://github.com/Liliana327)

Daniel Celis Tobon - [Github](https://github.com/danicelistobon)
