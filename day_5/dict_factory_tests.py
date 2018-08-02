import unittest
from day_5.DictFactory import DictFactory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.read_only_dict = DictFactory \
            .factory({'a': 1, 'b': 2, 'c': 3},
                     read=True, add=False,
                     modify=False, delete=False)

        self.read_modify_dict = DictFactory \
            .factory({'a': 1, 'b': 2, 'c': 3},
                     read=True, modify=True,
                     add=False, delete=False)

        self.read_modify_del_dict = DictFactory \
            .factory({'a': 1, 'b': 2, 'c': 3},
                     read=True, modify=True,
                     add=False, delete=True)

        self.read_modify_add_del_dict = DictFactory \
            .factory({'a': 1, 'b': 2, 'c': 3},
                     read=True, modify=True,
                     add=True, delete=True)

    def test_reading(self):
        self.assertEqual((1, 2, 3), (self.read_only_dict.a,
                                     self.read_only_dict.b,
                                     self.read_only_dict.c))

        self.assertEqual((1, 2, 3), (self.read_modify_dict.a,
                                     self.read_modify_dict.b,
                                     self.read_modify_dict.c))

        self.assertEqual((1, 2, 3), (self.read_modify_del_dict.a,
                                     self.read_modify_del_dict.b,
                                     self.read_modify_del_dict.c))
        #
        # self.assertEqual((1, 2, 3), (self.read_modify_add_del_dict.a,
        #                              self.read_modify_add_del_dict.b,
        #                              self.read_modify_add_del_dict.c))

    def test_modifying(self):
        self.read_modify_dict.a = 0
        self.read_modify_del_dict.a = 0
        self.read_modify_add_del_dict.a = 0

        self.assertEqual(0, self.read_modify_dict.a)
        self.assertEqual(0, self.read_modify_del_dict.a)
        self.assertEqual(0, self.read_modify_add_del_dict.a)

        with self.assertRaises(AttributeError):
            self.read_only_dict.a = 0

    def test_delete_attribute(self):
        with self.assertRaises(AttributeError):
            del self.read_only_dict.a

        with self.assertRaises(AttributeError):
            del self.read_modify_dict.a

        self.assertIsNone(self.read_modify_del_dict.__delattr__('a'))

        self.assertIsNone(self.read_modify_add_del_dict.__delattr__('a'))

        with self.assertRaises(AttributeError):
            del self.read_modify_del_dict.a

        with self.assertRaises(AttributeError):
            del self.read_modify_add_del_dict.a

    def test_adding(self):
        with self.assertRaises(AttributeError) as e:
            self.read_only_dict.new_attribute = "smth new"

        with self.assertRaises(AttributeError) as e:
            self.read_modify_dict.new_attribute = "smth new"

        with self.assertRaises(AttributeError) as e:
            self.read_modify_del_dict.new_attribute = "smth new"

        self.read_modify_add_del_dict.d = 4
        self.assertEqual(self.read_modify_add_del_dict.d, 4)


if __name__ == '__main__':
    unittest.main()
