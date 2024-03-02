#!/usr/bin/python3
"""This is the logic and entry point for the AirBnB command interpreter."""
import cmd
import models
from parser.argument_parser import (
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
        and prints the ID"""
        try:
            cls = parse_args(args, ClassArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            obj = class_map[cls]()
            obj.save()
            print(obj.ID)

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and ID
        """
        try:
            cls, ID = parse_args(args,
                                 ClassArgument,
                                 IDArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            try:
                key = f"{cls}.{ID}"
                obj = models.storage.objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")
                return False

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID (save the
        change into the JSON file)"""
        try:
            cls, ID = parse_args(arg,
                                 ClassArgument,
                                 IDArgument)
        except ValueError as e:
            print(str(e))
            return False
        else:
            key = f"{cls}.{ID}"
            obj = models.storage.objects.get(key, None)
            if obj is None:
                print("** no instance found **")
                return False
            obj.remove()

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name"""
        try:
            cls = parse_args(args, ClassArgument)
        except ValueError as e:
            cls = None
        finally:
            if not cls:
                result = [str(models.storage.objects[key])
                          for key
                          in models.storage.objects]
            else:
                result = [str(models.storage.objects[key])
                          for key
                          in models.storage.objects
                          if key.startswith(cls + '.')]
            print(result)

    def do_update(self, args):
        """Updates an instance based on the class name and ID by adding
        or updating attribute (save the change into the JSON file)"""
        try:
            cls, ID, attr, value = parse_args(args,
                                              ClassArgument,
                                              IDArgument,
                                              AttributeArgument,
                                              ValueArgument)
        except ValueError as e:
            print(str(e))
        else:
            key = f"{cls}.{ID}"
            obj = models.storage.objects.get(key, None)
            if obj is None:
                print("** no instance found **")
                return False
            setattr(obj, attr, cast(value))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
