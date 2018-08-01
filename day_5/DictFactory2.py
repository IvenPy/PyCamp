class ReadOnlyDict:
    def __init__(self, wrapped_dict):
        self._set_initials('wrapped_dict', wrapped_dict)

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
            self.wrapped_dict[item] = ReadOnlyDict(value)
        return self.wrapped_dict.get(item)

    def __delattr__(self, item):
        raise AttributeError("You cannot delete attributes in ReadOnlyDict")


class ReadModifyDict:
    def __init__(self, wrapped_dict):
        self._set_initials('wrapped_dict', wrapped_dict)

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

    def __getattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} wasn't found".format(item))
        value = self.wrapped_dict.get(item)
        if isinstance(value, dict):
            self.wrapped_dict[item] = ReadModifyDict(value)
        return self.wrapped_dict.get(item)

    def __delattr__(self, item):
        raise AttributeError("You cannot delete attributes in ReadOnlyDict")

    def __setattr__(self, key, value):
        if key not in self.wrapped_dict:
            raise AttributeError("You cannot add attributes in ReadModifyDict")
        if isinstance(value, dict):
            value = ReadModifyDict(value)
        self.wrapped_dict[key] = value
        print(key)


class ReadModifyDeleteDict:
    def __init__(self, wrapped_dict):
        self._set_initials('wrapped_dict', wrapped_dict)

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
        if key not in self.wrapped_dict:
            raise AttributeError("You cannot add attributes in ReadModifyDict")
        if isinstance(value, dict):
            value = ReadModifyDeleteDict(value)
        self.wrapped_dict[key] = value

    def __getattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} wasn't found".format(item))
        value = self.wrapped_dict.get(item)
        if isinstance(value, dict):
            self.wrapped_dict[item] = ReadModifyDeleteDict(value)
        return self.wrapped_dict[item]

    def __delattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} doesn't exist".format(item))
        else:
            self.wrapped_dict.pop(item)


class ReadModifyAddDeleteDict:
    def __init__(self, wrapped_dict):
        self._set_initials('wrapped_dict', wrapped_dict)

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
        if isinstance(value, dict):
            value = ReadModifyDeleteDict(value)
        self.wrapped_dict[key] = value
        print(key)

    def __getattr__(self, item):
        value = self.wrapped_dict[item]
        if not isinstance(value, dict):
            self.wrapped_dict.update({item: {}})
        if isinstance(value, dict):
            self.wrapped_dict[item] = ReadModifyDeleteDict(value)
        return self.wrapped_dict[item]

    def __delattr__(self, item):
        if item not in self.wrapped_dict:
            raise AttributeError("Attribute {} doesn't exist".format(item))
        else:
            self.wrapped_dict.pop(item)


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
