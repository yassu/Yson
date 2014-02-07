#!/usr/bin/env python3 


__all__ = ['load_from_text', 'load']

def load_from_text(yjtext):
    """
    input : text with YJson format
    output: python buildin structure
    """

def load(f):
    """
    input: file object with YJson format
    output: python buildin structure
    """

class YJsonItem:
    def get_data(self):
        """ return data which this object sgin """

    @staticmethod
    def parse_with_next(text):
        """
        return this object which sign first part of text.
        if text do not sign this object perfectly, return None.
        """

class YJString(YJsonItem):
    """ String format with YJsonItem """

class YJNumber(YJsonItem):
    """ Number format widht YJsonItem """

class YJBool(YJsonItem):
    """ Boolean format with YJsonItem """

class YJList(YJsonItem):
    """ List format with YJsonItem """


