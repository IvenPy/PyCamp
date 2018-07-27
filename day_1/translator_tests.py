import unittest
import day_1
from unittest import mock
from day_1 import translator
from day_1.translator import TranslitError

class MyTestCase(unittest.TestCase):

    def test_translator_not_found(self):
        with self.assertRaises(TranslitError) as e:
            unkown_trans = translator.get_translator("lalala", "blablabla")

    def test_getting_known_translator(self):
        known_translator = translator.get_translator("en", "rus")
        self.assertDictEqual(translator.EN_TO_RUS, known_translator)

    def test_fail_on_unknown_symbol(self):
        with self.assertRaises(TranslitError) as e:
            en_rus_trans = translator.get_translator("en", "rus")
            translator.translate(en_rus_trans, "خنده دار")

    def test_right_translitiration(self):
        en_rus_trans = translator.get_translator("rus", "en")
        text = "Среди ублюдков был артист, в кожанном плаще, мертвый анархист"
        translit_text = translator.translate(en_rus_trans, text)

        self.assertEqual(translit_text,
                         "Sredi ublyudkov bul artist,"
                         " v kozhannom plashe, mertvuy anarhist")


if __name__ == '__main__':
    unittest.main()
