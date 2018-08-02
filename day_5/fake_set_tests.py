import unittest
from day_5.FakeSet import FakeSet


class MyTestCase(unittest.TestCase):

    def test_unique_elements(self):
        s = FakeSet('12345321')
        self.assertTrue(s == FakeSet('12345'))

    def test_add_element(self):
        s = FakeSet()
        s.add('1')
        s = s + '2'
        self.assertTrue('1' in s)
        self.assertTrue('2' in s)
        with self.assertRaises(ValueError) as e:
            s.add([])

    def test_remove_element(self):
        s = FakeSet('1')
        s.remove('1')
        self.assertFalse(s.contains('1'))

    def test_update_fakeset(self):
        s1 = FakeSet('123')
        s2 = FakeSet('456')
        s1.update(s2)
        self.assertTrue(s1, {range(1, 7)})
        s3 = set('789')
        s1.update(s3)
        self.assertTrue(s3, {range(1, 10)})

    def test_operations(self):
        s1 = FakeSet('123')
        s2 = FakeSet('456')
        s3 = s1 + s2
        self.assertTrue(s3 == FakeSet('123456'))

    def test_clear(self):
        s1 = FakeSet('1234')
        s1.clear()
        self.assertEqual(s1, FakeSet())

    def test_union(self):
        s1 = FakeSet('123')
        s2 = FakeSet('456')
        s3 = set('789')
        s4 = s1.union(s3)
        self.assertEqual(s1.union(s2), FakeSet('123456'))
        self.assertEqual(s1.union(s2).union(s3), FakeSet('123456789'))

    def test_update(self):
        s1 = FakeSet('12')
        s2 = FakeSet('34')
        s3 = set('56')
        s1.update(s2)
        self.assertEqual(s1, FakeSet('1234'))
        s1.update(s3)
        self.assertEqual(s1, FakeSet('123456'))

    def test_difference(self):
        s1 = FakeSet('1234')
        s2 = FakeSet('12')
        s3 = FakeSet('34')
        s1 = s1.difference(s2)
        self.assertEqual(s1, FakeSet('34'))
        s1 = s1.difference(s3)
        self.assertEqual(s1, FakeSet())


if __name__ == '__main__':
    unittest.main()
