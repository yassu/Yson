#!/usr/bin/env python3
from re import sub as _sub


def obtain_suitable_comment(text, reg):
    """
    remove part of matching reg
    """
    return _sub(reg, ' ', text)
