import collections


class FakeSet:
    def __init__(self, seq):
        self.inner_set = []
        for x in seq:
            if x not in self.inner_set:
                if isinstance(x, collections.Hashable):
                    self.inner_set.append(x)
                else:
                    break
        else:
            raise TypeError("{} not hashable".format(type(x)))

    def __contains__(self, item):
        if item in self.inner_set:
            return True

    def __xor__(self, other):
        if isinstance(other, FakeSet) \
                or isinstance(other, set):
            xor = [x for x in self.inner_set if x not in other]
            xor.extend([x for x in other if x not in self.inner_set])
            return FakeSet(xor)
        else:
            raise TypeError("Unsupported operand type + between {} and FakeSet".format(type(other)))

    def __and__(self, other):
        if isinstance(other, FakeSet) \
                or isinstance(other, set):
            intersection = [x for x in other if x in self.inner_set]
            return FakeSet(intersection)
        else:
            raise TypeError("Unsupported operand type + between {} and FakeSet".format(type(other)))

    def issubset(self, other):
        if isinstance(other, FakeSet) \
                or isinstance(other, set):
            for x in self.inner_set:
                if x in other:
                    return True
        else:
            raise TypeError("Unsupported operand type + between {} and FakeSet".format(type(other)))
        return False

    def pop(self):
        if len(self.inner_set):
            return self.inner_set.pop(-1)
        else:
            raise KeyError("Pop from empty FakeSet")

    def remove(self, element):
        try:
            self.inner_set.remove(element)
        except ValueError:
            raise