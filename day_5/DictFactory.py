class Permissions:
    def __init__(self, read, modify, add, delete):
        self.read = read
        self.modify = modify
        self.add = add
        self.delete = delete


class ReadOnlyDict(dict):
    def __init__(self, wrapped_dict):
        super(ReadOnlyDict, self).__init__(wrapped_dict)

    def __getattr__(self, item):
        if not super(ReadOnlyDict, self).__contains__(item):
            raise AttributeError("Key {} wasn't found".format(item))
        else:
            value = super(ReadOnlyDict, self).__getitem__(item)
            if isinstance(super(ReadOnlyDict, self).__getitem__(item), dict):
                super(ReadOnlyDict, self).__setitem__(item, ReadOnlyDict(value))
            return super(ReadOnlyDict, self).__getitem__(item)

    def __setattr__(self, key, value):
        raise AttributeError("You cannot add and modify attributes in ReadOnlyDict")

    def __delattr__(self, item):
        raise AttributeError("You cannot delete attributes in ReadOnlyDict")


class ReadModifyDict(dict):
    def __init__(self, wrapped_dict):
        super(ReadModifyDict, self).__init__(wrapped_dict)

    def __getattr__(self, item):
        if not super(ReadModifyDict, self).__contains__(item):
            raise AttributeError("Key {} wasn't found".format(item))
        else:
            value = super(ReadModifyDict, self).__getitem__(item)
            if isinstance(super(ReadModifyDict, self).__getitem__(item), dict):
                super(ReadModifyDict, self).__setitem__(item, ReadModifyDict(value))
            return super(ReadModifyDict, self).__getitem__(item)

    def __setattr__(self, key, value):
        if not super(ReadModifyDict, self).__contains__(key):
            raise AttributeError("You cannot add attributes in ReadModifyDict")
        else:
            value_in_dict = super(ReadModifyDict, self).__getitem__(key)
            if isinstance(key, ReadModifyDict):
                pass
            elif isinstance(value_in_dict, dict):
                super(ReadModifyDict, self).__setitem__(key, ReadModifyDict(value_in_dict))
            super(ReadModifyDict, self).__setitem__(key, value)

    def __delattr__(self, item):
        raise AttributeError("You cannot delete attributes in ReadModifyDict")


class ReadModifyDeleteDict(dict):
    def __init__(self, wrapped_dict):
        super(ReadModifyDeleteDict, self).__init__(wrapped_dict)

    def __getattr__(self, item):
        if not super(ReadModifyDeleteDict, self).__contains__(item):
            raise AttributeError("Key {} wasn't found".format(item))
        else:
            value = super(ReadModifyDeleteDict, self).__getitem__(item)
            if isinstance(super(ReadModifyDeleteDict, self).__getitem__(item), dict):
                super(ReadModifyDeleteDict, self).__setitem__(item, ReadModifyDeleteDict(value))
            return super(ReadModifyDeleteDict, self).__getitem__(item)

    def __setattr__(self, key, value):
        if not super(ReadModifyDeleteDict, self).__contains__(key):
            raise AttributeError("You cannot add attributes in ReadModifyDeleteDict")
        else:
            value_in_dict = super(ReadModifyDeleteDict, self).__getitem__(key)
            if isinstance(key, ReadModifyDict):
                pass
            elif isinstance(value_in_dict, dict):
                super(ReadModifyDeleteDict, self).__setitem__(key, ReadModifyDict)
            super(ReadModifyDeleteDict, self).__setitem__(key, value)

    def __delattr__(self, item):
        if not super(ReadModifyDeleteDict, self).__contains__(item):
            raise AttributeError("You cannot delete attributes in ReadModifyDeleteDict")
        else:
            super(ReadModifyDeleteDict, self).__delitem__(item)


class ReadModifyAddDeleteDict(dict):
    def __init__(self, wrapped_dict):
        super(ReadModifyAddDeleteDict, self).__init__(wrapped_dict)

    def __getattr__(self, item):
        if not super(ReadModifyAddDeleteDict, self).__contains__(item):
            raise AttributeError("Key {} wasn't found".format(item))
        else:
            value = super(ReadModifyAddDeleteDict, self).__getitem__(item)
            if isinstance(super(ReadModifyAddDeleteDict, self).__getitem__(item), dict):
                super(ReadModifyAddDeleteDict, self).__setitem__(item, ReadModifyAddDeleteDict(value))
            return super(ReadModifyAddDeleteDict, self).__getitem__(item)

    def __setattr__(self, key, value):
        if not super(ReadModifyAddDeleteDict, self).__contains__(key):
            super(ReadModifyAddDeleteDict, self).__setitem__(key, value)
        value_in_dict = super(ReadModifyAddDeleteDict, self).__getitem__(key)
        if isinstance(key, ReadModifyDict):
            pass
        elif isinstance(value_in_dict, dict):
            super(ReadModifyAddDeleteDict, self).__setitem__(key, ReadModifyDict)
        super(ReadModifyAddDeleteDict, self).__setitem__(key, value)

    def __delattr__(self, item):
        if not super(ReadModifyAddDeleteDict, self).__contains__(item):
            raise AttributeError("You cannot delete attributes in ReadModifyDeleteDict")
        else:
            super(ReadModifyAddDeleteDict, self).__delitem__(item)


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
