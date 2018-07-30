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
