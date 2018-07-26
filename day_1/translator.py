"""
This module provides transliterations between to languages.
However for know it is only english and russian languages.
If you want others too create dictionary that matches letters from one
language to another.
For more information read functions docs or read code.

    Example:
        translator = get_translator('rus', 'en')
        text = 'Эта строка будет подверена транслитерации'
        translited_text = translate(translator, text)


        text == 'Eta stroka budet podverena transliteracii'

Enjoy
"""

import string

RUS_TO_EN_EXT = {
    'г': 'g', 'ё': 'yo',
    'м': 'm', 'ф': 'f',
    'х': 'h', 'ч': 'ch',
    'ш': 'sh', 'щ': 'sh',
    'ы': 'u', 'й': 'y',
    'ю': 'yu', 'я': 'ya',
    'з': 'z', 'ж': 'zh',
    'ь': '', 'ъ': ''
}

EN_TO_RUS_EXT = {
    'z': 'з', 'c': 'k',
    'h': 'х', 'f': 'ф',
    'g': 'ж', 'm': 'м',
    'q': 'ку', 'u': 'у',
    'w': 'в', 'x': 'кс',
    'y': 'у'
}

EX_RUS = "Эта строка будет подверена транслитерации"\
    .replace(' ', '').lower()

EX_EN = "Eta stroka budet podverena transliteracii"\
    .replace(' ', '').lower()

# creating transliterator from rus to en language

RUS_TO_EN = {EX_RUS[i]: EX_EN[i] for i in range(len(EX_RUS))}
RUS_TO_EN.update(RUS_TO_EN_EXT)

# creating transliterator from en to rus language

EN_TO_RUS = {EX_EN[i]: EX_RUS[i] for i in range(len(EX_EN))}
EN_TO_RUS.update(EN_TO_RUS_EXT)


class TranslitError(Exception):
    def __init__(self, message):
        super(TranslitError, self).__init__(message)


def get_translator(lan_from, lan_to):
    """
    Return translator that matches symbols from one language to another

    Args:
        lan_from: language name from what you want to transliterate
        lan_to: language name that you want to transliterate to.

    Returns: dict of matching letters

    """
    if lan_from == 'rus' and lan_to == 'en':
        return RUS_TO_EN

    elif lan_from == 'en' and lan_to == 'rus':
        return EN_TO_RUS

    raise TranslitError("There is no {} to {} translator"
                        .format(lan_from, lan_to))


def translate(translator, text):
    """
    Translates text with specified translator.
    Throws exception if unknown symbol for translator occurs in text

    Args:
        translator: dict that matches symbols from one language to another
        text: text to transliterate

    Returns: string representation of translated text

    """
    translit_text = []
    for letter in text:
        up = False

        if letter.isupper():
            up = True
        letter = letter.lower()

        if letter in string.punctuation or letter.isdigit() or letter.isspace():
            translit_text.append(letter)
        elif letter in translator:
            if up:
                new_let = translator[letter.lower()].upper()
                translit_text.append(new_let)
            else:
                translit_text.append(translator[letter])
        else:
            raise TranslitError("Can't translate symbol: {}".format(letter))
    return ''.join(translit_text)


def main():
    text = ''
    with open('text', 'r') as f:
        text = f.read()
    print("Native text: \n" + text)
    translator = get_translator('rus', 'en')
    translit_text = translate(translator, text)
    print("Translated text: \n" + translit_text)


if __name__ == "__main__":
    main()
