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
    l1 = [1, 2, 3, [4, 5, 6, 7]]
    t = (1, 2, 3)
    g = (x for x in range(3))
    print(list(chain(l1, t, g)))
