import types


def reverse_iter(collection):
    """
    Generator objects from collection in reverse order
    Args:
        collection:

    Returns:

    """
    if isinstance(type(collection), types.GeneratorType):
        collection = tuple(collection)
    for x in collection[::-1]:
        yield x


if __name__ == '__main__':
    pass
