#!/usr/bin/env python3 
from re import sub as _sub

DUMMY_CHAR = (' ', '\n', '\r')

def except_first_spaces(text):
    """ delete head spaces """
    while len(text) > 0 and text[0] in DUMMY_CHAR:
        text = text[1:]
    return text

def obtain_suitable_comment(text, reg):
    """
    remove part of matching reg
    """
    return _sub(reg, ' ', text)

