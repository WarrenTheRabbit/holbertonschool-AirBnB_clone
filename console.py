#!/usr/bin/python3
"""This is the logic and entry point for the AirBnB command interpreter."""
import cmd
import models
from parser.argument_parser import (
    format_objectoriented_to_command_language,
    parse_args,
    cast
)
from parser.arguments import (
    ClassArgument,
    IDArgument,
    AttributeArgument,
    ValueArgument,
)

class_map = {
    "BaseModel": models.base_model.BaseModel,
    "User": models.user.User,
    "State": models.state.State,
    "Review": models.review.Review,
    "Place": models.place.Place,
    "City": models.city.City,
    "Amenity": models.amenity.Amenity
}


class HBNBCommand(cmd.Cmd):
    """This is the command interpreter for the AirBnB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        try:
            cls = parse_args(args, ClassArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            obj = class_map[cls]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and id
        """
        try:
            cls, id_ = parse_args(args,
                                  ClassArgument,
                                  IDArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            try:
                key = f"{cls}.{id_}"
                obj = models.storage.objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")
                return False

    def do_count(self, arg):
        """Count the number of instances of a class."""
        try:
            cls = parse_args(arg, ClassArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            print(len([key
                       for key
                       in models.storage.objects
                       if key.startswith(cls + '.')
                       ]))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)"""
        try:
            cls, id_ = parse_args(arg,
                                  ClassArgument,
                                  IDArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            key = f"{cls}.{id_}"
            obj = models.storage.objects.get(key, None)
            if obj is None:
                print("** no instance found **")
                return False
            obj.remove()

    def precmd(self, line):
        """Preprocess the command line for special syntax."""
        try:
            line = format_objectoriented_to_command_language(line)
        except ValueError as e:
            pass
        finally:
            return line

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name"""
        try:
            cls = parse_args(args, ClassArgument)
        except ValueError as e:
            if str(e) == "** class doesn't exist **":
                print(str(e))
            if str(e) == "** class name missing **":
                print([str(models.storage.objects[key])
                       for key
                       in models.storage.objects])
        else:
            print([str(models.storage.objects[key])
                   for key
                   in models.storage.objects
                   if key.startswith(cls + '.')])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        try:
            cls, id_, attr, value = parse_args(args,
                                               ClassArgument,
                                               IDArgument,
                                               AttributeArgument,
                                               ValueArgument)
        except ValueError as e:
            print(str(e))
        else:
            key = f"{cls}.{id_}"
            obj = models.storage.objects.get(key, None)
            if obj is None:
                print("** no instance found **")
                return False
            setattr(obj, attr, cast(value))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
