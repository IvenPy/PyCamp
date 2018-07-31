class Integers:
    Index = None

    def __init__(self):
        if not self.Index:
            Integers.Index = 0

    def __iter__(self):
        return self

    def __next__(self):
        Integers.Index += 1
        return Integers.Index


if __name__ == '__main__':
    pass
