def cast(value):
    try:
        return int(value)
    except ValueError as e:
        return str(value)


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
