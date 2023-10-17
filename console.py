#!/usr/bin/python3
"""
This module defines 'HBNBCommand' class
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    commnad interpreter that manages the AirBnB objects.
    """

    prompt = '(hbnb) '
    __valid_classes = [
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
    ]

    def default(self, line):
        """ Method called on an input line when
        the command prefix is not recognized """
        actions = {
            r'^all\(.*\)$': self.do_all,
            r'^count\(.*\)$': self.do_count,
            r'^show\(.*\)$': self.do_show,
            r'^destroy\(.*\)$': self.do_destroy,
            r'^update\(.*\)$': self.do_update
        }

        args = line.split('.')
        if len(args) == 2:
            for action in actions.keys():
                match = re.search(pattern=action, string=args[1])
                if match:
                    text_args = match.group()

                    # r'^update\(.*, \{.*\}\)$': self.__update_from_dict
                    pattern = r'\(.*, \{.*\}\)$'
                    match = re.search(pattern=pattern, string=text_args)
                    if match:
                        txt_args = str(match.group())
                        params = eval("[" + txt_args[1:-1] + "]")
                        dct = params[-1]
                        dct['id'] = params[0]
                        dct['class'] = args[0]
                        return self.__update_from_dict(dct)
                    else:
                        pattern = r'\(.*\)$'
                        match = re.search(pattern=pattern, string=text_args)
                        if match:
                            txt_args = str(match.group())
                            txt_args = txt_args[1:-1].replace(',', ' ')
                            txt_args = "{} {}".format(args[0], txt_args)
                            return actions[action](txt_args)

        return super().default(line)

    def do_count(self, line):
        """
        Retrieves the number of instances of a class: <class name>.count().
        """
        args = line.strip().split('.')
        count = 0

        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel, saves it to a JSON file
        and prints the 'id'
        """
        if not cls:
            print('** class name missing **')
        elif cls not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        else:
            print((eval(cls)()).id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1].replace('"', ''))
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        arg = arg.strip()
        objs_dict = storage.all()

        if arg and arg not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        else:
            objs_list = []
            for obj in objs_dict.values():
                if not arg:
                    objs_list.append(obj.__str__())
                elif type(obj).__name__ == arg:
                    objs_list.append(obj.__str__())
            print(objs_list)

    def __update_from_dict(self, dct):
        """Updates an instance based on the class name and id
        by adding or updating an attribute"""

        if not dct.get('class', False):
            print('** class name missing **')
        elif dct['class'] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif not dct.get('id', False):
            print('** instance id missing **')
        else:
            key = "{}.{}".format(dct['class'], dct['id'])
            if key not in storage.all():
                print('** no instance found **')
            else:
                forbiden_update = ['id', 'created_at', 'updated_at', 'class']
                for attr, value in dct.items():
                    if attr not in forbiden_update:
                        obj = storage.all()[key]
                        if attr in obj.__dict__:
                            value = type(obj.__dict__[attr])(value)
                        obj.__setattr__(attr, value)
                        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute
        Usage: update <class name> <id> <attribute name>
        "<attribute value>\""""
        args_arr = split(arg.strip(), posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            elif len(args_arr) == 2:
                print('** attribute name missing **')
            elif len(args_arr) == 3:
                print('** value missing **')
            else:
                forbiden_update = ['id', 'created_at', 'updated_at']
                if args_arr[2] not in forbiden_update:
                    attr = args_arr[2].replace('"', '')
                    value = eval(args_arr[3])
                    obj = storage.all()[key]
                    if attr in obj.__dict__:
                        value = eval(type(obj.__dict__[attr]).__name__)(value)
                    obj.__setattr__(attr, value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
