

I = 0  # global index


def integers():
    """
    Singleton generator of integers

    Returns:
        int
    """
    global I
    while True:
        I += 1
        yield I


if __name__ == '__main__':
    pass
