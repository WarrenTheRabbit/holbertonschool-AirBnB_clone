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

        cls, *id_list = arg.split(maxsplit=1)
        id = ' '.join(id_list)
        if cls not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")
            return False

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

        cls, *id_list = arg.split()
        id = ' '.join(id_list)
        if cls not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")
            return False

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

        arg_ls = arg.split()
        cls = None

        if arg_ls:
            cls = arg_ls[0]

        if cls and cls not in class_map:
            print("** class doesn't exist **")
            return False

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

        args_ls = [None, None, None, None]

        for index, value in enumerate(arg.split()):
            if index > 3:
                continue
            args_ls[index] = value

        cls_name = args_ls[0]
        id = args_ls[1]
        att_name = args_ls[2]
        attr_val = args_ls[3]

        if cls_name not in class_map:
            print("** class doesn't exist **")
            return False

        if not id:
            print("** instance id missing **")
            return False

        if not att_name:
            print("** attribute name missing **")
            return False

        if not attr_val:
            print("** value missing **")
            return False

        key = f"{cls_name}.{id}"
        all_objs = models.storage.all()
        obj = all_objs.get(key, None)

        if not obj:
            print(key)
            print("** no instance found **")
            return False

        if hasattr(obj, att_name):
            attr = getattr(obj, att_name, None)
            T = type(attr)
        else:
            if (attr_val.startswith("\"") and
               attr_val.endswith("\"")):
                attr_val = attr_val[1:-1]
                T = type("")
            else:
                T = type(1)

        setattr(obj, att_name, T(attr_val))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
