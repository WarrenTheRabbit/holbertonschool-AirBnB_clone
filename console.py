#!/usr/bin/python3
"""This is the logic and entry point for the AirBnB command interpreter."""
import cmd
import models


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in class_map:
            print("** class doesn't exist **")
        else:
            obj = class_map[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return False

        cls, id = arg.split()
        if cls not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")

        key = f"{cls}.{id}"
        all_objs = models.storage.all()
        obj = all_objs.get(key, None)
        if not obj:
            print("** no instance found **")
            return False
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return False

        cls, *id = arg.split()
        if cls not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")

        key = f"{cls}.{id}"
        all_objs = models.storage.all()
        obj = all_objs.get(key, None)
        if not obj:
            print("** no instance found **")
            return False

        obj.remove(key)

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            result = [str(models.storage.objects[key])
                      for key
                      in models.storage.objects
                      ]
        else:
            result = [str(models.storage.objects[key])
                      for key
                      in models.storage.objects
                      if key.startswith(arg + '.')
                      ]
        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return False

        cls, id, name, value, *_ = arg.split()
        if cls not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")
            return False

        if not name:
            print("** attribute name missing **")
            return False

        if not value:
            print("** value missing **")

        key = f"{cls}.{id}"
        all_objs = models.storage.all()
        obj = all_objs.get(key, None)
        if not obj:
            print("** no instance found **")
            return False

        if hasattr(obj, name):
            attr = getattr(obj, name)
            T = type(attr)
            setattr(obj, name, T(value))
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
