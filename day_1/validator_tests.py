import unittest
from day_1 import validator


class MyTestCase(unittest.TestCase):
    def test_wrong_keys(self):
        data = validator.get_context({'name', 'id', 'nick', 'action'})
        template = "{name} {id} and {action} {job}"
        with self.assertRaises(KeyError) as e:
            validator.check_validation(template, data)

    def test_correct_template(self):
        data = validator.get_context({'name', 'id', 'nick', 'action'})
        template = "{name} {id} {nick} {action}"
        filled_str = template.format(**data)
        self.assertEqual(validator.check_validation(template, data), filled_str)


if __name__ == '__main__':
    unittest.main()
