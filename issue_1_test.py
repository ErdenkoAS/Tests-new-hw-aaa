# -*- coding: utf-8 -*-
"""issue_1_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IbpMQUC5yVIWRm5Th52bmZ_dNa1dhvoU
"""

LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе
    Примеры:
    >>> encode('SOS')
    '... --- ...'
    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode('123')
    '.----   ..--- ...--'
    >>> encode('')
    ''
    >>> encode(123)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    >>> encode('VERY LONG...') # doctest: +ELLIPSIS
    '...- ... ...'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)