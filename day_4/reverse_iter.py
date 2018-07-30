def reverse_iter(collection):
    """
    Generator objects from collection in reverse order
    Args:
        collection:

    Returns:

    """
    for x in collection[::-1]:
        yield x


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print(list(reverse_iter(l)))
