import utils
from abc import ABC, abstractmethod


class Classes:
    options = utils.class_map()


class Validator:

    def __init__(self, error):
        self.error = error

    def __get__(self, instance, owner):
        return getattr(instance, '__value')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, '__value', value)

    @abstractmethod
    def validate(self, value):
        pass


class NotNone(Validator):

    def __init__(self, *, error):
        super().__init__(error)

    def validate(self, value):
        if value is None:
            raise ValueError(self.error)


class OneOf(Validator):

    def __init__(self, *, error, choices):
        super().__init__(error)
        self.choices = choices

    def validate(self, value):
        if not value:
            raise ValueError("** class name missing **")
        if value not in self.choices:
            raise ValueError(self.error)


class IDArgument():
    """The id argument is used to represent the id of an instance."""
    value = NotNone(error="** instance id missing **")

    def __init__(self, value):
        self.value = value


class AttributeArgument:
    """The attribute argument is used to represent the attribute
    of an instance."""
    value = NotNone(error="** attribute name missing **")

    def __init__(self, value):
        self.value = value


class ValueArgument:
    """The value argument is used to represent the value of an instance."""
    value = NotNone(error="** value missing **")

    def __init__(self, value):
        self.value = value


class ClassArgument(Classes):
    value = OneOf(error="** class doesn't exist **",
                  choices=[*Classes.options])

    def __init__(self, value):
        self.value = value
