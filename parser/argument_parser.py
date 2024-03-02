import re


def cast(value):
    try:
        return int(value)
    except ValueError as e:
        return str(value)


def format_objectoriented_to_command_language(oo_command):
    """Given user input in object-oriented-like syntax, convert it
    to the  command language used by the console program.

    For example,
        ohject-oriented syntax                  command languagw
        ----------------------------------      -------------------------
        User.all()                          --> all User
        User.count()                        --> count User
        User.update("id", "attr", "value")  --> update User id attr value
    """
    if not re.match(r'^\w+\.\w+\(.*\)$', oo_command):
        raise ValueError("Invalid object-oriented syntax")
    try:
        replacements = '().,"'
        oo_command = "".join([char
                              if char not in replacements
                              else " "
                              for char in oo_command])
        parts = oo_command.split()
        cls = parts[0]
        command = parts[1]
        args = " ".join(parts[2:])
        return f"{command} {cls} {args}"
    except Exception as e:
        raise ValueError("Incomplete object-oriented syntax")


def parse_args(args: str, *expectations):
    """Parse the provided arguments and validate them."""
    parsed_args = get_argument_values(args, len(expectations))
    validated_args = [validator(value=arg)
                      for arg, validator
                      in zip(parsed_args, expectations)]
    if len(validated_args) == 1:
        return parsed_args[0]
    else:
        return parsed_args


def get_argument_values(args, expected_number):
    """If the provided arguments are fewer than what was expected,
    represent the missing arguments with None."""
    split_args = args.split() + ([None] * expected_number)
    split_args = split_args[:expected_number]
    return split_args
