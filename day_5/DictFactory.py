import copy


class ReadOnlyDict:
    """
    ReadOnlyDict is decorator over class dict. Instead
    of using [] to get required items you can access to them using
    .name_of_attribute.
    Note that you can't create new attributes or change existing one in this class.
    At attempt to modify, delete or add attribute AttributeError will be occurred
    Also accessing, deleting, modifying to not existing attributes will cause AttributeError
    """
    def __init__(self, wrapped_dict):
        self._set_initials('wrapped_dict', copy.deepcopy(wrapped_dict))

    def _set_initials(self, name, value):
        """ This function remove redundancy while creating
            an object at __init__
        Args:
            name (str): namespace in this class
            value (obj): value of this namespace
        Returns:
            object: prepared base object with __setattr__
        """
        object.__setattr__(self, name, value)

    def __setattr__(self, key, value):
        raise AttributeError("You cannot add and modify attributes in ReadOnlyDict")

    def __getattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} wasn't found".format(item))
        value = self.wrapped_dict.get(item)
        if isinstance(value, dict):
            self.wrapped_dict[item] = self.__class__(value)
        return self.wrapped_dict.get(item)

    def __delattr__(self, item):
        raise AttributeError("You cannot delete attributes in ReadOnlyDict")


class ReadModifyDict(ReadOnlyDict):
    """
    ReadModifyDict is a heir of ReadOnlyDict
    with one change - now you can modify attributes of your instance.
    Exception AttributeError won't occur at attempt to set new value to existing attribute
    """
    def __init__(self, wrapped_dict):
        super().__init__(wrapped_dict)

    def __setattr__(self, key, value):
        if key not in self.wrapped_dict:
            raise AttributeError("You cannot add attributes in {}".format(type(self)))
        if isinstance(value, dict):
            value = self.__class__(value)
        self.wrapped_dict[key] = value


class ReadModifyDeleteDict(ReadModifyDict):
    """
    ReadModifyDict is a heir of ReadModifyDict
    with one change - now you can delete attributes of your instance.
    """
    def __init__(self, wrapped_dict):
        super().__init__(wrapped_dict)

    def __delattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} doesn't exist".format(item))
        else:
            self.wrapped_dict.pop(item)


class ReadModifyAddDeleteDict(ReadModifyDeleteDict):
    """
    ReadModifyAddDeleteDict is a heir of ReadModifyDeleteDict
    with one change - now you can add new attributes of your instance
    Exception won't occur at deleting, modifying and accessing to existing attribute.
    At adding new attribute two things can happen:

        1. If the object to which the attribute is added to dict or ReadModifyAddDeleteDict,
            or any other type that allow to add attributes, adding attribute will happen
            successfully.

        2. If the object is built-in type or other type that doesn't allow
            adding attribute exception will be thrown
    """
    def __init__(self, wrapped_dict):
        super().__init__(wrapped_dict)

    def __setattr__(self, key, value):
        if isinstance(value, dict):
            value = self.__class__(value)
        self.wrapped_dict[key] = value


class DictFactory(object):
    @staticmethod
    def factory(wrapped_dict, read=True,
                modify=False, add=False, delete=False):

        if read and not modify \
                and not add and not delete:
            return ReadOnlyDict(wrapped_dict)

        if read and modify \
                and not add and not delete:
            return ReadModifyDict(wrapped_dict)

        if read and modify \
                and delete and not add:
            return ReadModifyDeleteDict(wrapped_dict)

        if read and modify and delete and add:
            return ReadModifyAddDeleteDict(wrapped_dict)

        else:
            raise ValueError("There is no such class with"
                             " parameters read={], modify={},"
                             " add={}, delete=[}"
                             .format(read, modify, add, delete))
