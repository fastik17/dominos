from enum import Enum


class DjangoEnum(Enum):
    """Extend this enumeration for all your models choice fields.
    Exactly you need to use choices method for your choice field
    """
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

    @classmethod
    def to_docs(cls, should_include_values=False):
        """Convert enum to string to be used in docstring

        :param should_include_values: should include values instead of names
        :return: comma-separated string of choices
        """
        if should_include_values:
            return ', '.join([f'`{v.value}`' for v in cls])
        return ', '.join([f'`{v.name}`' for v in cls])
