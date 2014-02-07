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
    def __init__(self, text):
        if len(text) < 2 or text[0] != '"' or text[-1] != '"':
            raise TypeError()
        self._text = text[1:-1]
    
    def get_data(self):
        return self._text

    @staticmethod
    def parse_with_next(text):
        if len(text) < 2 or text[1:].find('"') == -1:   # illegal pattern
            return None

        sep_ind = 1 + text[1:].find('"')
        obj = YJString('"' + text[:sep_ind + 1])
        text = text[:sep_ind]
        return obj, text

    def __repr__(self):
        return 'YJString<{}>'.format(self._text)

class YJNumber(YJsonItem):
    """ Number format widht YJsonItem """

class YJBool(YJsonItem):
    """ Boolean format with YJsonItem """

class YJList(YJsonItem):
    """ List format with YJsonItem """


def yjstring_test():
    print('yjstring test ====== ')
    text = '"abcdef"'
    print('given: {}'.format(text))
    print('YJString.parse_with_next method returns {}.'.format(
            YJString.parse_with_next(text)))

    print('illegal test ===')
    text = 'abcdef"'
    print('given: {}'.format(text))
    print('YJString.parse_with_next method returns {}.'.format(
            YJString.parse_with_next(text)))    # -> Error

yjstring_test()
