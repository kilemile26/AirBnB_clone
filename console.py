#!/usr/bin/python3
"""
Module: console
Command interpreter for the AirBnB clone project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "
    valid_classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']


    def emptyline(self):
        """
        Empty line handler.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Create command to create a new instance of a class, saves it and prints the id.
        """
        args = arg.split()
        if not arg or args[0] not in HBNBCommand.valid_classes:
            print("** class missing **")
            return
        else:
            try:
                new_instance = eval(arg[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
                
    def do_count(self, arg):
        """
        Count command to retrieve the number of instances of a class.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                count = sum(1 for obj in storage.all().values() if type(obj).__name__ == class_name)
                print(count)
            except NameError:
                print("** class doesn't exist **")


    def do_show(self, arg):
        """
        Show command to display an instance.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                obj = storage.all().get(key, None)
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                obj = storage.all().get(key, None)
                if obj:
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        All command to display all instances.
        """
        args = arg.split()
        obj_list = []
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                all_instances = eval(class_name).all()
                for obj in all_instances:
                    obj_list.append(str(obj))
                    print(obj_list)
                    """
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        else:
            try:
                class_name = args[0]
                for key, value in storage.all().items():
                    if key.startswith(class_name):
                        obj_list.append(str(value))
                if obj_list:
                    print(obj_list)
                else:
                    print("** class doesn't exist **")
                    """
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update command to update an instance.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                obj = storage.all().get(key, None)
                if obj:
                    attr_name = args[2]
                    if len(args) >= 4:
                        attr_value = args[3]
                        setattr(obj, attr_name, attr_value)
                        storage.save()
                    else:
                        print("** value missing **")
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")



    def do_update_dict(self, arg):
        """
        Update command to update an instance based on its ID using a dictionary.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                obj = storage.all().get(key, None)
                if obj:
                    if len(args) >= 3:
                        updates = eval(args[2])
                        if isinstance(updates, dict):
                            for key, value in updates.items():
                                setattr(obj, key, value)
                            storage.save()
                        else:
                            print("** updates must be a dictionary **")
                    else:
                        print("** dictionary missing **")
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")


    class_dict = [
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review',
            ]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
