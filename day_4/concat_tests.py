import unittest
from day_4.collection_concat import chain, Chain


class MyTestCase(unittest.TestCase):
    def test_chain(self):
        l = [1, 2]
        t = (3, 4)
        g = (x for x in range(5, 7))
        result = list(chain(l, t, g))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_nested_chain(self):
        l = [1, [2]]
        t = (3, (4, ))
        result = list(chain(l, t))
        self.assertEqual(result, [1, 2, 3, 4])

    def test_chain_class(self):

        l = [1, 2]
        t = (3, 4)
        g = (x for x in range(5, 7))
        result = list(Chain(l, t, g))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
