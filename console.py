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
        elif not arg in class_map:
            print("** class doesn't exist **")
        else:
            obj = class_map[arg]()
            obj.save()
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
