class Integers():
    Index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.Index += 1
        return self.Index


if __name__ == '__main__':
    pass
