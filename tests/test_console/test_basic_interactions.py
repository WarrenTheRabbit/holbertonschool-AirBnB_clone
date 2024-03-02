#!/usr/bin/python3
from console import HBNBCommand
from unittest.mock import patch
import textwrap
import unittest
import io


class TestPrompt(unittest.TestCase):
    """
    This class attempts to test the behaviour of the console in an
    implementation agnostic manner. It has not been entirely successful.
    However, this underlying philosophy is why direct calls to the
    methods that implement the commands are not made.

    ### Issues

    1) The mocked input is not written to the output.
    2) It uses initialization to redirect stdin and stdout, and further makes
    use of an instance attribute, 'use_rawinput', to prevent calls to `input`.
    """

    def test_that_console_displays_correct_prompt(self):
        mocked_input = io.StringIO("")
        output = io.StringIO()

        cmd = HBNBCommand(stdin=mocked_input,
                          stdout=output)
        cmd.use_rawinput = False

        cmd.cmdloop()
        self.assertEqual(output.getvalue(), "(hbnb) ")

    def test_help_command(self):
        user_input = "help"
        expected = "(hbnb) \n"
        expected += "Documented commands (type help <topic>):\n"
        expected += "========================================\n"
        expected += "EOF  all  count  create  destroy  help  quit  show  update\n\n"  # noqa
        expected += "(hbnb) "

        mocked_input = io.StringIO(user_input)
        output = io.StringIO()

        cmd = HBNBCommand(stdin=mocked_input,
                          stdout=output)
        cmd.use_rawinput = False
        cmd.cmdloop()

        self.assertMultiLineEqual(output.getvalue(), expected)

    def test_quit_command(self):
        user_input = "quit"
        mocked_input = io.StringIO(user_input)
        output = io.StringIO()

        cmd = HBNBCommand(stdin=mocked_input,
                          stdout=output)
        cmd.use_rawinput = False
        cmd.cmdloop()

        self.assertEqual(output.getvalue(), "(hbnb) ")

    def test_that_EOF_terminates_program(self):
        user_input = "EOF"
        mocked_input = io.StringIO(user_input)
        output = io.StringIO()

        cmd = HBNBCommand(stdin=mocked_input,
                          stdout=output)
        cmd.use_rawinput = False
        cmd.cmdloop()

        self.assertEqual(output.getvalue(), "(hbnb) ")

    def test_that_help_topics_work(self):
        user_input = "help EOF\nhelp quit\nhelp help"
        mocked_input = io.StringIO(user_input)
        output = io.StringIO()

        cmd = HBNBCommand(stdin=mocked_input,
                          stdout=output)
        cmd.use_rawinput = False
        cmd.cmdloop()

        self.assertEqual(output.getvalue(), textwrap.dedent("""\
            (hbnb) EOF command to exit the program (Ctrl+D)
            (hbnb) Quit command to exit the program
            (hbnb) List available commands with "help" or detailed help with "help cmd".\n"""  # noqa
            """\
            (hbnb) """))


if __name__ == "__main__":
    unittest.main()
