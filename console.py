#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_count(self, line):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == line:
                count = count + 1
        print(count)

    def do_create(self, line):
        """ Creates an instance according to a given class """
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[args[0]]()
            print(my_model.id)
            my_model.save()

    def do_show(self, line):
        """ Shows string representation of an instance passed """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance passed """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """ Prints string represention of all instances of a given class """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        args = line.split(',')

        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3].strip('"'))
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
