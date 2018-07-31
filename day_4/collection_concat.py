

class Chain:
    def __init__(self, *args):
        self.__args = args
        self.__outer_index = 0
        self.__inner_index = 0

    def __iter__(self):
        yield from chain(self.__args)




def chain(*args):
    """
    Generator of all collections passed in arguments.
    Supports nested collections

    Args:
        *args: collections

    Returns:
        object
    """
    for collection in args:
        for x in collection:
            try:
                iterator = iter(x)
                yield from chain(x)
            except TypeError:
                yield x



if __name__ == '__main__':
    pass
