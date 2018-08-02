import collections
import copy


class FakeSet:
    def __init__(self, seq=''):
        self.__inner_set = []
        for x in seq:
            if x not in self.__inner_set:
                if isinstance(x, collections.Hashable):
                    self.__inner_set.append(x)
                else:
                    raise TypeError("{} not hashable".format(type(x)))

    def __contains__(self, item):
        return item in self.__inner_set

    def contains(self, item):
        return self.__contains__(item)

    def __eq__(self, other):
        if isinstance(other, FakeSet) or isinstance(other, set):
            for x in other:
                if x not in self.__inner_set:
                    return False
            for x in self.__inner_set:
                if x not in other:
                    return False
        else:
            return False
        return True

    def check_is_compatible(self, other, operand):
        if isinstance(other, FakeSet) \
                or isinstance(other, set):
            return
        else:
            raise TypeError("Unsupported operand type {} between {} and FakeSet"
                            .format(operand, type(other)))

    def __str__(self):
        return "{" + ", ".join(self.__inner_set) + "}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, FakeSet) \
                or isinstance(other, set):
            return self.union(other)
        else:
            self.add(other)
            return self

    def __sub__(self, other):
        self.remove(other)

    def update(self, other):
        for x in other:
            self.add(copy.deepcopy(x))

    def isdisjoinset(self, other):
        self.check_is_compatible(other, '')
        return True if not self.intersection(other) else False

    def issuperset(self, other):
        return other.issubset(self)

    def __copy__(self):
        return FakeSet(copy.copy(self.__inner_set))

    def copy(self):
        return self.__copy__()

    def add(self, item):
        if item not in self.__inner_set:
            if isinstance(item, collections.Hashable):
                self.__inner_set.append(item)
            else:
                raise ValueError("Can't add unhashable object {} to FakeSet"
                                 .format(item))

    def symmetric_difference(self, other):
        xor = [x for x in self.__inner_set if x not in other]
        xor.extend([x for x in other if x not in self.__inner_set])
        return FakeSet(xor)

    def symmetric_difference_update(self, other):
        symm_diff = self.symmetric_difference(other)
        for x in symm_diff:
            self.add(x)

    def clear(self):
        self.__inner_set.clear()

    def union(self, other):
        new_set = FakeSet(copy.deepcopy(self.__inner_set))
        new_set.update(other)
        return new_set

    def difference(self, other):
        self.check_is_compatible(other, '')
        return FakeSet([x for x in self.__inner_set
                        if x not in other.__inner_set])

    def __xor__(self, other):
        self.symmetric_difference(other)

    def intersection(self, other):
        self.check_is_compatible(other, 'intersection')
        intersection = [x for x in other if x in self.__inner_set]
        return FakeSet(intersection)

    def __and__(self, other):
        return self.intersection(other)

    def __iter__(self):
        for x in self.__inner_set:
            yield x

    def issubset(self, other):
        self.check_is_compatible(other, 'issubset')
        for x in self.__inner_set:
            if x in other:
                return False
        return True

    def pop(self):
        if len(self.__inner_set):
            return self.__inner_set.pop(-1)
        else:
            raise KeyError("Pop from empty FakeSet")

    def __len__(self):
        return len(self.__inner_set)

    def remove(self, element):
        try:
            self.__inner_set.remove(element)
        except ValueError:
            raise
