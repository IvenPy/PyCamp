class Yarange():
    """
    Infinite cycle generator of integers
    """

    def __init__(self, start, end):
        self.__start = start
        self.__i = start - 1
        self.__end = end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i < self.__end:
            return self.__i
        else:
            self.__i = self.__start
            return self.__i


if __name__ == '__main__':
    pass
