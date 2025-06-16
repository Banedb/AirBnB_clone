#!/usr/bin/python3
"""Command Line Interface for HBNB application."""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import ast
import cmd
import re
import shlex

classes = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """Main command line interpreter class."""

    prompt = "(hbnb) "

    def default(self, line):
        """Overrides command not found error for dot notation commands."""
        pattern = r'^(?:([\w]+))?\.(\w+)\((.*)\)$'
        match = re.match(pattern, line)

        if match:
            cls, command, args = match.groups()
            if command == "update" and "{" in args and "}" in args:
                args = args.replace(",", " ", 1)
            else:
                args = args.replace(",", " ")
            # print(args)
            command = getattr(self, f"do_{command}", None)
            if not command:
                print(f"*** Unknown syntax: {line}")
            elif not cls:
                print("** class name missing **")
            elif args:
                command(cls + " " + args)
            else:
                command(cls)
        else:
            print(f"*** Unknown syntax: {line}")

    def do_all(self, line):
        """Prints all string representation of all instances."""
        if not line or shlex.split(line)[0] in classes:
            all_objs = storage.all()
            obj_list = [
                str(all_objs[key]) for key in all_objs if not line
                or key.split(".")[0] == shlex.split(line)[0]
            ]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Retrieves the number of instances of a class."""
        name = self.parse_args(line, level="name")
        if name:
            count = 0
            all_objs = storage.all()
            for key in all_objs:
                if key.split(".")[0] == name:
                    count += 1
            print(count)

    def do_create(self, line):
        """Creates new instance of a class, saves it and prints the id."""
        name = self.parse_args(line, level="name")
        if name:
            cls = classes[name]
            new = cls()
            new.save()
            print(new.id)

    def do_destroy(self, line):
        """Destroys an instance."""
        obj = self.parse_args(line, level="id")
        if obj:
            obj.delete()

    def do_EOF(self, line):
        """Handles the end of file (EOF) marker"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_show(self, line):
        """Displays the instance matching class and id."""
        obj = self.parse_args(line, level="id")
        if obj:
            print(obj)

    def do_update(self, line):
        """Updates an instance and saves the change into the JSON file."""
        obj = self.parse_args(line, level="attr")
        if obj:
            dict_match = re.search(r'({.*})', line)
            dict_str = dict_match.group(1) if dict_match else None
            if dict_str:
                dict_str = ast.literal_eval(dict_str)
                for key in dict_str:
                    setattr(obj, key, dict_str[key])
            else:
                args = shlex.split(line)
                try:
                    args[3] = ast.literal_eval(args[3])
                except Exception:
                    pass
                setattr(obj, args[2], args[3])
            obj.save()

    def emptyline(self):
        """Overrides emptyline() and does nothing on empty line"""
        pass

    def parse_args(self, line, level=""):
        """Parses arguments to cmd and returns the class name or target object
        Args:
            line (str): The input command line.
            level (str): Determines the validation depth:
                - "name": checks only the class name value.
                - "id": checks class name and id values.
                - "attr": checks class name, id and attribute values.

            Returns:
                The class name or the object, or None if validation fails.
        """
        args = shlex.split(line)

        # check name
        if not args:
            print("** class name missing **")
            return None
        if args[0] not in classes:
            print("** class doesn't exist **")
            return None
        if level == "name":
            return args[0]

        # check id
        if len(args) < 2:
            print("** instance id missing **")
            return None
        if f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return None

        # check attributes
        if level != "id":
            if len(args) < 3:
                print("** attribute name missing **")
                return None
            elif len(args) < 4:
                print("** value missing **")
                return None
        return storage.all()[f"{args[0]}.{args[1]}"]

    do_exit = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
