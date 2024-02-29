#!/usr/bin/python3
"""This is the logic and entry point for the AirBnB command interpreter."""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
