#!/usr/bin/python3
""" Make the entry point to CMD """
import cmd
import json
from models import storage
from models.base_model import BaseModel
import shlex

class HBNBCommand(cmd.Cmd):
    """ Contain the commmanns of ours console

        Args:
            Inheritance from the class cmd
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ If there is empty line in the programm """
        pass

    # Ctrl + d = Quit the program
    do_EOF = do_quit

    def do_create(self, arg):
        """ Create un object instance """
        if not arg:
            print ("** class name missing **")
        elif arg != "BaseModel":
            print ("** class doesn't exist **")
        else:
            new_base = BaseModel()
            storage.save()
            print (new_base.id)

    def do_show(self, arg):
        """ Show the class """
        show_list = []
        show_list = shlex.split(arg)

        # if, there are not arguments return the function and print
        if not arg:
            print ("** class name missing **")
            return

        # Verify the len of the list
        if len(show_list) == 2:
            key = str(show_list[0] + "." + show_list[1])
        else:
            key = str(show_list[0])

        # Different options about cases
        if show_list[0] not in HBNBCommand.classes:
            print ("** class doesn't exist **")
        elif len(show_list) <= 1:
            print("** instance id missing **")


        else:
            # Try show all storage in otherwise print the error
            try:
                print(storage.all()[key])
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """ Print all the objects of the representation of the class"""
        key = str(arg)

        if not arg or arg:
            print(storage.all())
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Destroy instance based in classnmae and id """
        del_list = shlex.split(arg)

        if not arg:
            print ("** class name missing **")
            return

        # Verify the len of the list
        if len(del_list) == 2:
            key = str(del_list[0] + "." + del_list[1])
        else:
            key = str(del_list[0])

        # Different options about cases
        if del_list[0] not in HBNBCommand.classes:
            print ("** class doesn't exist **")
        elif len(del_list) <= 1:
            print("** instance id missing **")
        else:
            # Try show all storage in otherwise print the error
            try:
                del storage.all()[key]
            except:
                print("** no instance found **")

    def do_update(self, arg):
        """ Update the data of the json """
        update_list = shlex.split(arg)

        if not arg:
            print ("** class name missing **")
            return

            # Verify the len of the list
        if len(update_list) == 2:
            key = str(update_list[0] + "." + update_list[1])
        else:
            key = str(update_list[0])

        # Different options about cases
        if update_list[0] not in HBNBCommand.classes:
            print ("** class doesn't exist **")
        elif len(update_list) <= 1:
            print ("** instance id missing **")
        elif len(update_list) == 2:
            print ("** attribute name missing ** ")
        elif len(update_list) == 3:
            print ("** value missing **")

        else:
            # update <class name> <id> <attribute name> "<attribute value>"
            #             0         1         2                 3
            try:
                storage.all()[str(key + update_list[2])] = update_list[3]
            except:
                print("** no instance found **")


if __name__ == "__main__":
    """ Link the files """
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
